{
  "title": "高级数学分析RAG文档",
  "description": "包含完整数学分析知识体系的检索增强生成文档",
  "version": "2.0",
  "knowledge_graph": {
    "nodes": [
      {
        "id": "real_system",
        "label": "实数系统",
        "properties": {
          "definitions": [
            {
              "id": "def1",
              "text": "戴德金分割：将有理数集Q划分为两个非空集合A和B，满足A中每个元素小于B中所有元素",
              "formal": "A∪B=Q, A∩B=∅, ∀a∈A,∀b∈B⇒a<b"
            },
            {
              "id": "def2",
              "text": "上确界：集合S的最小上界，记作supS",
              "formal": "1) ∀x∈S, x≤supS; 2) ∀ε>0, ∃x∈S, x>supS-ε"
            }
          ],
          "theorems": [
            {
              "id": "thm1",
              "name": "确界存在定理",
              "statement": "非空有上界的实数子集必有上确界",
              "proof": "通过戴德金分割构造，取所有上界集合的下界"
            }
          ]
        }
      },
      {
        "id": "sequence_limit",
        "label": "数列极限",
        "properties": {
          "definitions": [
            {
              "id": "def3",
              "text": "ε-N定义：∀ε>0, ∃N∈ℕ, 当n>N时|aₙ-L|<ε",
              "symbolic": "(∀ε>0)(∃N∈ℕ)(n>N ⇒ |aₙ-L|<ε)"
            }
          ],
          "theorems": [
            {
              "id": "thm2",
              "name": "柯西收敛准则",
              "statement": "数列收敛当且仅当∀ε>0, ∃N, ∀m,n>N有|aₘ-aₙ|<ε",
              "proof_strategy": "必要性由三角不等式，充分性用确界定理"
            },
            {
              "id": "thm3",
              "name": "Bolzano-Weierstrass定理",
              "statement": "有界数列必有收敛子列",
              "proof": "二分法构造单调子列"
            }
          ],
          "examples": [
            {
              "id": "ex1",
              "problem": "证明lim(n→∞)(1+1/n)ⁿ=e",
              "solution": "先证单调递增，再证有上界，利用二项式展开"
            }
          ]
        }
      },
      {
        "id": "function_limits",
        "label": "函数极限",
        "properties": {
          "definitions": [
            {
              "id": "def4",
              "text": "ε-δ定义：limₓ→ₐ f(x)=L ⇔ ∀ε>0, ∃δ>0, 0<|x-a|<δ ⇒ |f(x)-L|<ε",
              "variants": [
                {
                  "type": "左极限",
                  "definition": "x→a⁻时成立"
                },
                {
                  "type": "无穷极限",
                  "definition": "a=∞时的修改定义"
                }
              ]
            }
          ],
          "techniques": [
            {
              "id": "tech1",
              "name": "夹逼定理",
              "statement": "若g(x)≤f(x)≤h(x)且lim g=lim h=L，则lim f=L",
              "application": "常用于证明limₓ→₀ x sin(1/x)=0"
            }
          ]
        }
      },
      {
        "id": "derivatives",
        "label": "微分学",
        "properties": {
          "theorems": [
            {
              "id": "thm4",
              "name": "费马定理",
              "statement": "若f在c点可导且取得极值，则f'(c)=0",
              "proof": "用左右导数相等证明"
            },
            {
              "id": "thm5",
              "name": "泰勒定理",
              "statement": "f(x)=Σ[f⁽ⁿ⁾(a)/n!](x-a)ⁿ + Rₙ(x)",
              "remainder": [
                {
                  "type": "拉格朗日余项",
                  "form": "Rₙ(x)=f⁽ⁿ⁺¹⁾(ξ)/(n+1)! (x-a)ⁿ⁺¹"
                },
                {
                  "type": "佩亚诺余项",
                  "form": "Rₙ(x)=o((x-a)ⁿ)"
                }
              ]
            }
          ],
          "applications": [
            {
              "id": "app1",
              "name": "洛必达法则",
              "conditions": [
                "0/0或∞/∞型",
                "分子分母在去心邻域可导",
                "导数比的极限存在"
              ],
              "example": "limₓ→₀ (sinx/x)=1"
            }
          ]
        }
      },
      {
        "id": "integration",
        "label": "积分学",
        "properties": {
          "definitions": [
            {
              "id": "def5",
              "text": "达布积分：通过上下积分相等定义",
              "relation": "等价于黎曼积分当f有界"
            }
          ],
          "theorems": [
            {
              "id": "thm6",
              "name": "积分中值定理",
              "statement": "∃ξ∈[a,b], ∫ₐᵇ f(x)dx=f(ξ)(b-a)",
              "visualization": "曲线下面积等于某点函数值与区间长度的乘积"
            }
          ],
          "advanced": [
            {
              "id": "adv1",
              "topic": "反常积分",
              "types": [
                {
                  "name": "第一类（无限区间）",
                  "example": "∫₁^∞ (1/x²)dx=1"
                },
                {
                  "name": "第二类（无界函数）",
                  "example": "∫₀¹ (1/√x)dx=2"
                }
              ]
            }
          ]
        }
      }
    ],
    "edges": [
      {
        "source": "real_system",
        "target": "sequence_limit",
        "relation": "确界定理→证明柯西准则"
      },
      {
        "source": "sequence_limit",
        "target": "function_limits",
        "relation": "海涅定理连接数列极限与函数极限"
      },
      {
        "source": "function_limits",
        "target": "derivatives",
        "relation": "连续性是可导性的必要条件"
      },
      {
        "source": "derivatives",
        "target": "integration",
        "relation": "微积分基本定理连接微分与积分"
      }
    ]
  },
  "problem_sets": [
    {
      "level": "基础",
      "problems": [
        {
          "id": "p1",
          "statement": "用ε-δ定义证明limₓ→₂ (3x-1)=5",
          "hint": "取δ=ε/3"
        },
        {
          "id": "p2",
          "statement": "求f(x)=x³在x=1处的导数",
          "solution": "3"
        }
      ]
    },
    {
      "level": "进阶",
      "problems": [
        {
          "id": "p3",
          "statement": "证明f(x)=x²在R上一致连续但在Rⁿ上不一致连续",
          "key_step": "利用导数有界性"
        },
        {
          "id": "p4",
          "statement": "计算∫eˣ sinx dx",
          "method": "分部积分法"
        }
      ]
    }
  ],
  "visual_resources": {
    "figures": [
      {
        "id": "fig1",
        "description": "函数极限的ε-δ图示",
        "elements": [
          "坐标平面",
          "函数曲线",
          "a点的去心邻域",
          "L±ε带形区域"
        ]
      }
    ]
  },
  "historical_notes": [
    {
      "concept": "极限理论",
      "contributors": [
        {
          "name": "柯西",
          "contribution": "严格的ε-δ定义"
        },
        {
          "name": "魏尔斯特拉斯",
          "contribution": "算术化处理"
        }
      ]
    }
  ]
}
{
  "title": "综合数学分析RAG文档",
  "description": "包含单变量分析、多元微积分和微分方程的完整知识体系",
  "version": "3.0",
  "knowledge_graph": {
    "nodes": [
      // 保留原有实数系统、数列极限等内容...
      
      {
        "id": "multivariable",
        "label": "多元函数",
        "properties": {
          "definitions": [
            {
              "id": "def_mv1",
              "text": "偏导数：固定其他变量，对某一变量的导数",
              "notation": "∂f/∂xᵢ = limₕ→₀ [f(x₁,...,xᵢ+h,...,xₙ)-f(x)]/h"
            },
            {
              "id": "def_mv2",
              "text": "梯度：函数在各方向偏导数组成的向量",
              "notation": "∇f = (∂f/∂x₁, ..., ∂f/∂xₙ)",
              "geometric": "指向函数增长最快的方向"
            }
          ],
          "theorems": [
            {
              "id": "thm_mv1",
              "name": "链式法则（多元版本）",
              "statement": "若z=f(x₁,...,xₙ), xᵢ=gᵢ(t)，则dz/dt = Σ(∂f/∂xᵢ)(dxᵢ/dt)",
              "matrix_form": "D(f∘g)(a) = Df(g(a))·Dg(a)"
            },
            {
              "id": "thm_mv2",
              "name": "隐函数定理",
              "statement": "若F(x,y)=0且∂F/∂y≠0，则存在y=f(x)",
              "application": "用于方程组的隐式求导"
            }
          ]
        }
      },
      {
        "id": "multiple_integral",
        "label": "多重积分",
        "properties": {
          "types": [
            {
              "id": "type_mi1",
              "name": "二重积分",
              "definition": "∬_D f(x,y) dA = lim_(‖P‖→0) Σ f(xᵢ*,yᵢ*)ΔAᵢ",
              "computation": [
                {
                  "method": "累次积分",
                  "example": "∬_[a,b]×[c,d] f(x,y) dxdy = ∫_a^b (∫_c^d f(x,y) dy) dx"
                }
              ]
            },
            {
              "id": "type_mi2",
              "name": "三重积分",
              "physical": "质量计算：∭_E ρ(x,y,z) dV"
            }
          ],
          "theorems": [
            {
              "id": "thm_mi1",
              "name": "变量替换公式",
              "statement": "∬_D f(x,y) dxdy = ∬_D' f(u,v)|J| dudv",
              "jacobian": "J = ∂(x,y)/∂(u,v) 为雅可比行列式"
            },
            {
              "id": "thm_mi2",
              "name": "高斯公式（散度定理）",
              "statement": "∭_E (∇·F) dV = ∯_S F·n dS",
              "application": "流体力学中的流量计算"
            }
          ]
        }
      },
      {
        "id": "diff_equations",
        "label": "微分方程",
        "properties": {
          "classification": [
            {
              "type": "常微分方程(ODE)",
              "subtypes": [
                {
                  "name": "一阶线性",
                  "form": "y' + p(x)y = q(x)",
                  "solution": "积分因子法"
                },
                {
                  "name": "二阶常系数",
                  "form": "ay'' + by' + cy = f(x)",
                  "solution": [
                    "齐次解：特征方程法",
                    "特解：待定系数法/参数变异法"
                  ]
                }
              ]
            },
            {
              "type": "偏微分方程(PDE)",
              "examples": [
                {
                  "name": "热方程",
                  "form": "∂u/∂t = k∇²u",
                  "physical": "热传导过程"
                },
                {
                  "name": "拉普拉斯方程",
                  "form": "∇²u = 0",
                  "application": "电势分布"
                }
              ]
            }
          ],
          "solution_methods": [
            {
              "id": "method_ode1",
              "name": "分离变量法",
              "example": "解dy/dx = y/x → ∫dy/y = ∫dx/x"
            },
            {
              "id": "method_pde1",
              "name": "傅里叶级数法",
              "application": "解波动方程"
            }
          ]
        }
      }
    ],
    "edges": [
      // 原有关系...
      {
        "source": "derivatives",
        "target": "multivariable",
        "relation": "单变量导数是偏导数的特例"
      },
      {
        "source": "multivariable",
        "target": "multiple_integral",
        "relation": "梯度与线积分的关系"
      },
      {
        "source": "multiple_integral",
        "target": "diff_equations",
        "relation": "格林函数用于解PDE"
      }
    ]
  },
  "problem_sets": [
    {
      "level": "多元函数",
      "problems": [
        {
          "id": "p_mv1",
          "statement": "求f(x,y)=x²y + sin(xy)在(π,1)处的梯度",
          "solution": "∇f = [2xy + ycos(xy), x² + xcos(xy)]_(π,1) = [2π-1, π²+π]"
        },
        {
          "id": "p_mv2",
          "statement": "用拉格朗日乘数法求x²+y²在x+y=1下的极值",
          "key_step": "解方程组∇f=λ∇g, g=0"
        }
      ]
    },
    {
      "level": "多重积分",
      "problems": [
        {
          "id": "p_mi1",
          "statement": "计算∬_D (x+y) dxdy，D由y=x²和y=4围成",
          "solution": "∫_{-2}^2 ∫_{x²}^4 (x+y) dydx = 256/15"
        },
        {
          "id": "p_mi2",
          "statement": "球坐标计算∭_E z dV，E为上半球x²+y²+z²≤1, z≥0",
          "method": "∫₀^{2π}∫₀^{π/2}∫₀¹ ρ³ cosφ sinφ dρdφdθ"
        }
      ]
    },
    {
      "level": "微分方程",
      "problems": [
        {
          "id": "p_ode1",
          "statement": "解初值问题：y' + y = eˣ, y(0)=1",
          "solution": "y(x) = (eˣ + e⁻ˣ)/2"
        },
        {
          "id": "p_pde1",
          "statement": "用分离变量法解∂u/∂t = k ∂²u/∂x², u(0,t)=u(L,t)=0",
          "approach": "设u(x,t)=X(x)T(t)，解特征值问题"
        }
      ]
    }
  ],
  "applications": [
    {
      "domain": "物理学",
      "examples": [
        {
          "concept": "梯度",
          "application": "电场强度是电势的负梯度"
        },
        {
          "concept": "高斯公式",
          "application": "计算电场通量"
        }
      ]
    },
    {
      "domain": "机器学习",
      "examples": [
        {
          "concept": "多元函数极值",
          "application": "梯度下降法优化损失函数"
        },
        {
          "concept": "偏微分方程",
          "application": "图神经网络中的扩散过程"
        }
      ]
    }
  ]
}
{
  "title": "数学分析全景式RAG文档",
  "description": "从实数基础到微分方程的完整知识体系，包含理论-应用-历史三维度",
  "version": "4.0",
  "structure": {
    "foundations": ["实数系统", "极限理论", "连续性"],
    "core": ["微分学", "积分学", "级数理论"],
    "advanced": ["多元微积分", "微分方程", "测度论初步"]
  },
  "knowledge_base": {
    "concepts": [
      // ========== 基础部分 ==========
      {
        "id": "limit",
        "label": "极限",
        "definitions": [
          {
            "type": "ε-δ定义",
            "content": "函数极限的严格定义",
            "formal": "∀ε>0, ∃δ>0, 0<|x-a|<δ ⇒ |f(x)-L|<ε",
            "visual": "动态趋近动画链接"
          }
        ],
        "theorems": [
          {
            "name": "海涅定理",
            "statement": "函数极限存在当且仅当所有数列极限存在且相等",
            "usage": "连接函数与数列极限"
          }
        ]
      },
      
      // ========== 多元微积分 ==========
      {
        "id": "jacobian",
        "label": "雅可比矩阵",
        "definitions": [
          {
            "type": "矩阵形式",
            "content": "多元函数一阶偏导组成的矩阵",
            "example": "f:ℝⁿ→ℝᵐ的雅可比矩阵为m×n矩阵Jᵢⱼ=∂fᵢ/∂xⱼ"
          }
        ],
        "applications": [
          {
            "field": "机器学习",
            "example": "反向传播算法的核心计算工具"
          }
        ]
      },

      // ========== 微分方程 ==========
      {
        "id": "pde_classification",
        "label": "PDE分类",
        "types": [
          {
            "name": "椭圆型",
            "example": "拉普拉斯方程∇²u=0",
            "property": "描述稳态系统"
          },
          {
            "name": "抛物型",
            "example": "热方程∂u/∂t=k∇²u",
            "property": "描述扩散过程"
          }
        ]
      }
    ],
    
    "theorem_network": [
      {
        "source": "implicit_function",
        "target": "lagrange_multiplier",
        "relation": "隐函数定理证明拉格朗日乘数法"
      },
      {
        "source": "green",
        "target": "stokes",
        "relation": "格林定理是斯托克斯定理的特例"
      }
    ]
  },
  "learning_resources": {
    "problem_sets": {
      "basic": [
        {
          "type": "计算题",
          "problem": "求limₓ→∞ (1+1/x)ˣ",
          "method": "自然对数变形+洛必达法则"
        }
      ],
      "advanced": [
        {
          "type": "证明题",
          "problem": "证明康托尔集是不可数零测集",
          "hint": "使用对角线论证法"
        }
      ]
    },
    
    "visual_guides": [
      {
        "concept": "方向导数",
        "diagram": {
          "type": "3D曲面图",
          "elements": ["梯度向量", "等高线", "切平面"]
        }
      }
    ]
  },
  "historical_context": {
    "timeline": [
      {
        "era": "17世纪",
        "event": "牛顿-莱布尼茨创立微积分",
        "figures": ["牛顿", "莱布尼茨"]
      },
      {
        "era": "19世纪",
        "event": "柯西-魏尔斯特拉斯建立严格极限理论",
        "figures": ["柯西", "魏尔斯特拉斯"]
      }
    ]
  },
  "applications": {
    "physics": [
      {
        "concept": "散度定理",
        "use_case": "麦克斯韦方程组的积分形式推导"
      }
    ],
    "data_science": [
      {
        "concept": "梯度下降",
        "algorithm": "深度学习优化器的数学基础"
      }
    ]
  },
  "cross_references": {
    "prerequisites": {
      "real_analysis": ["集合论", "拓扑基础"]
    },
    "advanced_topics": {
      "manifold": ["微分几何", "广义相对论数学基础"]
    }
  }
}