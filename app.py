import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.legacy.callbacks import CallbackManager
from llama_index.llms.openai_like import OpenAILike
import matplotlib.pyplot as plt
import numpy as np
import re
import os

# Create an instance of CallbackManager
callback_manager = CallbackManager()

file_path = ".env"

# 读取文件内容
with open(file_path, 'r') as file:
    config = file.readlines()

# 将每行内容拆解为键值对
config_dict = {}
for line in config:
    if '=' in line:
        key, value = line.strip().split('=', 1)
        config_dict[key.strip()] = value.strip().strip('"')

# 打印读取的配置信息
api_base_url = config_dict.get("api_base_url")
model = config_dict.get("model")
api_key = config_dict.get("api_key")



llm =OpenAILike(model=model, api_base=api_base_url, api_key=api_key, is_chat_model=True,callback_manager=callback_manager)

st.set_page_config(page_title="数学分析助手", page_icon="🦜🔗")
st.title("数学分析助手")

# 初始化模型
@st.cache_resource
def init_models():
    embed_model = HuggingFaceEmbedding(
        model_name="/root/model/sentence-transformer"
    )
    Settings.embed_model = embed_model

    #用初始化llm
    Settings.llm = llm

    documents = SimpleDirectoryReader("/root/math_agent/data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    return query_engine

# 检查是否需要初始化模型
if 'query_engine' not in st.session_state:
    st.session_state['query_engine'] = init_models()

def greet2(question):
    response = st.session_state['query_engine'].query(question)
    return response

# 函数图像绘制相关功能
def plot_function(function_str, x_range=(-10, 10), num_points=1000):
    """
    绘制数学函数图像
    
    参数:
    function_str: 函数表达式字符串，例如 "x**2" 或 "np.sin(x)"
    x_range: x轴范围，默认为(-10, 10)
    num_points: 用于绘图的点数，默认为1000
    
    返回:
    matplotlib图形对象
    """
    # 创建一个新的图形
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # 创建x轴数据点
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    try:
        # 替换常见的数学函数表示为numpy函数
        func_str = function_str.replace('^', '**')
        for math_func in ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt']:
            if math_func in func_str:
                func_str = func_str.replace(math_func, f'np.{math_func}')
        
        # 计算y值
        y = eval(func_str)
        
        # 绘制函数
        ax.plot(x, y)
        ax.grid(True)
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # 设置标题和标签
        ax.set_title(f'函数: {function_str}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
        return fig
    except Exception as e:
        st.error(f"绘制函数时出错: {str(e)}")
        return None

def is_plot_request(message):
    """
    检查用户消息是否为绘制函数的请求
    
    参数:
    message: 用户消息字符串
    
    返回:
    如果是绘图请求，返回函数表达式；否则返回None
    """
    plot_patterns = [
        r'画出函数\s*[：:]\s*(.*?)$',
        r'绘制函数\s*[：:]\s*(.*?)$',
        r'画出\s*(.*?)的图像',
        r'绘制\s*(.*?)的图像',
        r'plot.*?function\s*[：:]\s*(.*?)$'
    ]
    
    for pattern in plot_patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return None
      
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "你好，我是数学分析助手，有什么我可以帮助你的吗？也可以让我绘制函数图像！\n 绘制图像请用以下格式:\n- '画出函数：x^2 + 2*x + 1'\n- '绘制函数：sin(x)'\n- '画出cos(x)的图像'\n- '绘制x^3 - 4*x的图像' "}]    

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "你好，我是数学分析助手，有什么我可以帮助你的吗？也可以让我绘制函数图像！\n 绘制图像请用以下格式:\n- '画出函数：x^2 + 2*x + 1'\n- '绘制函数：sin(x)'\n- '画出cos(x)的图像'\n- '绘制x^3 - 4*x的图像' "}]

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llama_index_response(prompt_input):
    return greet2(prompt_input)

# User-provided prompt
if prompt := st.chat_input("输入问题或者让我绘制函数图像"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # 检查是否为绘图请求
    function_expr = is_plot_request(prompt)
    if function_expr:
        with st.chat_message("assistant"):
            st.write(f"正在绘制函数: {function_expr}")
            fig = plot_function(function_expr)
            if fig:
                st.pyplot(fig)
                message = {"role": "assistant", "content": f"我已经绘制了函数 {function_expr} 的图像。"}
                st.session_state.messages.append(message)
            else:
                error_msg = "无法绘制该函数，请检查函数表达式是否正确。"
                st.write(error_msg)
                message = {"role": "assistant", "content": error_msg}
                st.session_state.messages.append(message)
    # 如果不是绘图请求，使用原有的响应生成逻辑
    elif st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_llama_index_response(prompt)
                placeholder = st.empty()
                placeholder.markdown(response)
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)