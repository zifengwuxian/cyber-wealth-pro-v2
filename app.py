import streamlit as st
from openai import OpenAI
import auth  # 导入同级目录下的 auth.py

# ==========================================
# 1. 页面配置与黑金皮肤 (High-End UI)
# ==========================================
st.set_page_config(
    page_title="赛博·财富架构师",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 注入 CSS：打造“彭博终端”风格
st.markdown("""
<style>
    /* 全局背景黑 */
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }
    /* 侧边栏样式 */
    section[data-testid="stSidebar"] {
        background-color: #16181C;
    }
    /* 按钮金 */
    .stButton>button {
        background: linear-gradient(45deg, #D4AF37, #FFD700);
        color: black;
        font-weight: bold;
        border: none;
        width: 100%;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
    }
    /* 输入框 */
    .stTextArea textarea, .stTextInput input {
        background-color: #262730;
        color: #FFD700; /* 输入文字也是金色 */
        border: 1px solid #4B4B4B;
    }
    /* 报告卡片样式 */
    .report-container {
        border: 1px solid #FFD700;
        background-color: #000000;
        padding: 25px;
        border-radius: 5px;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.1);
        font-family: 'Courier New', monospace;
        margin-top: 20px;
        font-size: 14px;
        line-height: 1.6;
    }
    .report-header {
        border-bottom: 1px dashed #FFD700;
        padding-bottom: 10px;
        margin-bottom: 15px;
        color: #D4AF37;
        font-size: 1.2em;
        font-weight: bold;
    }
    .score-badge {
        display: block;
        font-size: 3.5em;
        font-weight: 900;
        text-align: center;
        margin: 20px 0;
        letter-spacing: 5px;
        font-family: 'Impact', sans-serif;
        transform: rotate(-5deg);
        border: 3px solid currentColor;
        padding: 10px;
        border-radius: 10px;
        opacity: 0.9;
    }
    .score-S { color: #00FF00; text-shadow: 0 0 10px #00FF00; }
    .score-A { color: #D4AF37; text-shadow: 0 0 10px #D4AF37; }
    .score-B { color: #FFA500; }
    .score-C { color: #FF4500; }
    .score-D { color: #FF0000; }
    
    @media only screen and (max-width: 600px) {
        .score-badge {
            font-size: 2.5em;
        }
    }
    
    /* 隐藏 Streamlit 默认的右上角汉堡菜单和底部的 Footer，显得像原生 App */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 手机端适配 */
    @media (max-width: 600px) {
        /* 让标题在手机上更大更醒目 */
        h1 {
            font-size: 2rem !important;
            text-align: center;
        }
        /* 让图片说明文字大一点 */
        .stImageCaption {
            font-size: 1rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 统一发卡机验证逻辑
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/3d-fluency/94/money-bag-bitcoin.png", width=60)
    st.markdown("### 🔐 身份验证")
    
    # 状态管理：如果已经验证过，就不要再输密码了
    if "license_verified" not in st.session_state:
        st.session_state.license_verified = False
        st.session_state.card_type = ""

    if not st.session_state.license_verified:
        st.info("🔒 系统已加密，请获取卡密解锁")
        st.markdown("💰 **单次清醒卡：9.9元 (24小时)**")
        st.markdown("👑 **长期军师卡：39元 （月卡）**")
        st.markdown("---")
        input_key = st.text_input("请输入【赛博通行证】", type="password", help="获取方式请查看主页")
        st.markdown("(客服微信: liao13689209126)")
        if st.button("激活系统"):
            with st.spinner("正在连接赛博矩阵云端数据库..."):
                # 调用 auth.py 的验证函数，应用代号 'fortune'
                is_valid, msg, card_type = auth.check_license(input_key, 'fortune')
                
                if is_valid:
                    st.session_state.license_verified = True
                    st.session_state.card_type = card_type
                    st.success(msg)
                    st.rerun() # 刷新页面
                else:
                    st.error(msg)
    else:
        st.success(f"已激活: {st.session_state.card_type}")
        if st.button("退出登录"):
            st.session_state.license_verified = False
            st.rerun()

    st.markdown("---")
    st.caption("🤖 Powered by DeepSeek-V3 & CyberMatrix")

# ==========================================
# 3. 拦截逻辑：手机优先版 (Mobile First Layout)
# ==========================================
if not st.session_state.license_verified:
    st.title("💸 赛博·财富架构师")
    st.markdown("---")
    
    # --- 第一层：标题和痛点 (Hook) ---
    st.markdown("### 👁️ 为什么要测？")
    st.markdown("👇 **看看 AI 是如何一针见血骂醒这个\"想全职炒股\"的用户的：**")
    st.image("case_study.png", caption="真实案例：挽回50万止损的深度复盘", use_container_width=True)
    st.warning("⚠️ 警告：本系统只说真话，玻璃心请绕道。")
    
    st.markdown("---")
    
    # --- 第二层：转化和支付 (Action) ---
    st.markdown("### 🔓 立即解锁算力")
    
    with st.container():
        st.info("🔥 限时体验：**9.9元** / 24小时 (无限次)")
        
        with st.expander("👉 点击获取【财富通行证】(微信/支付宝)", expanded=False):
            st.write("1. 扫码支付 9.9 元")
            pay_tab1, pay_tab2 = st.tabs(["🟢 微信", "🔵 支付宝"])
            with pay_tab1:
                st.image("pay_wechat.png", width=200)
            with pay_tab2:
                st.image("pay_alipay.png", width=200)
            st.write("2. 支付备注 **【财神】**")
            st.write("3. 截图发给客服，秒发通行证密码")
            st.caption("客服微信：liao13689209126")
    
    # --- 第三层：输入框预告 ---
    st.text_input("请输入【赛博通行证】", placeholder="在此输入密码...", disabled=True)
    st.button("激活系统", disabled=True)
    
    st.stop()

# ==========================================
# 4. 核心功能：DeepSeek 接入
# ==========================================

# 从 Secrets 获取 API KEY (安全第一)
try:
    API_KEY = st.secrets["DEEPSEEK_API_KEY"]
    BASE_URL = "https://api.deepseek.com"
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
except Exception as e:
    st.error("⚠️ 系统配置错误：未找到 API Key。请在 Streamlit Secrets 中配置 DEEPSEEK_API_KEY。")
    st.stop()

# 核心 Prompt：赋予它毒舌且专业的灵魂
SYSTEM_PROMPT = """
你是一位【赛博财富架构师】。你的底层逻辑是：概率论、博弈论、行为经济学。
你说话风格：毒舌、冷酷、一针见血、使用金融术语，但最后会给出极其实用的建议。

【任务】
用户输入一个搞钱/职业/商业计划。
你要生成一份【赛博量化评估报告】，包含 HTML 标签。

【输出格式要求】
请直接输出以下 HTML 代码结构（不要输出 markdown 代码块标记）：

<div class="report-header">
    📊 PROJECT EVALUATION REPORT
    <span class="score-badge score-{RATING_LEVEL}">{SCORE}分 / {RATING_LEVEL}级</span>
</div>

<p><strong>01. 核心算法解析 (Algorithm Analysis)</strong><br>
> 胜率 (Win Rate): {WIN_RATE}%<br>
> 赔率 (Odds): {ODDS}<br>
> 破产概率 (Ruin Probability): {RUIN_PROB}%
</p>

<p><strong>02. 毒舌点评 (Critical Review)</strong><br>
{TOXIC_COMMENT} (请用尖锐的语言指出用户思维里的漏洞，比如幸存者偏差、沉没成本等)
</p>

<p><strong>03. 风险扫描 (Black Swan Scan)</strong><br>
⚠️ {RISK_1}<br>
⚠️ {RISK_2}
</p>

<p><strong>04. 优化/止损建议 (Action Items)</strong><br>
✅ {ADVICE_1}<br>
✅ {ADVICE_2}
</p>

【注意】
- {RATING_LEVEL} 只能是 S, A, B, C, D 之一。
- {SCORE} 是 0-100 的整数。
- 如果用户计划太离谱，请毫不留情地给 D 级。

【特别指令】
在"优化/止损建议"的最后一条，必须结合用户的痛点，暗示他需要提升效率或搞流量。
例如："别再用蛮力干活了，去学学如何用 AI 工具（如自动化文案、数据分析）来放大你的单位时间产出。"
"""

st.title("💸 赛博·财富架构师")
st.caption(f"当前用户身份: {st.session_state.card_type} | 算力全开")

user_query = st.text_area(
    "输入您的决策计划 (Project Protocol)", 
    height=150, 
    placeholder="例如：我有 50 万存款，想辞职全职炒股，能否实现财务自由？"
)

if st.button("🚀 RUN SIMULATION (启动推演)"):
    if not user_query:
        st.warning("⚠️ 输入为空，无法计算。")
    else:
        with st.spinner("🔄 正在接入全球市场数据库...正在进行蒙特卡洛模拟..."):
            try:
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_query},
                    ],
                    temperature=1.2, 
                    stream=False
                )
                report_html = response.choices[0].message.content
                
                # 渲染结果
                st.markdown(f"""
                <div class="report-container">
                    {report_html}
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ 算力连接失败: {e}")

# 底部
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #666; font-size: 12px;'>CYBER MATRIX WEALTH SYSTEM V2.0</div>", unsafe_allow_html=True)