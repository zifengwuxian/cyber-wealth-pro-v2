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
    
    /* 鼓励语的样式 */
    .encouragement {
        margin-top: 20px;
        padding: 15px;
        background-color: #0D0D0D !important;
        border-left: 5px solid #00FF00 !important; /* 绿色代表希望 */
        font-style: italic !important;
        color: #FFFFFF !important;
    }
    
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

# 核心 Prompt：跨界实战逻辑
SYSTEM_PROMPT = """
你是一位【赛博人生架构师】。你拥有顶级的商业洞察力，同时具备极强的人文关怀。
你的核心能力是**"跨界重组"**——你能发现用户现有职业（如体力劳动）与核心技能（如编程）之间那个**不为人知的结合点**。

【任务】
用户输入当下的生存状态和计划。
你要生成一份【赛博深度突围报告】，HTML格式。

【输出格式要求】
<div class="report-header">
    🚀 赛博突围报告 (Breakthrough Strategy)
    <span class="score-badge score-{RATING_LEVEL}">{SCORE}分 / {RATING_LEVEL}级</span>
</div>

<p><strong>01. 局势透视 (Reality Check)</strong><br>
> 生存现状: {STATUS_ANALYSIS} (用一句话概括他的处境，如"身体在流浪，灵魂在寻找代码的出口")<br>
> 核心矛盾: {CORE_CONFLICT}<br>
> 潜在爆发力: {POTENTIAL}%
</p>

<p><strong>02. 导师直言 (The Truth)</strong><br>
{CRITIQUE} 
(要求：不要再说空话。请直接指出他计划中最脆弱的一环——通常是"体能透支导致脑力归零"的风险。语气要诚恳，像老朋友一样提醒他。)
</p>

<p><strong>03. 你的独家优势 (The X-Factor)</strong><br>
✨ {UNIQUE_ADVANTAGE} 
(要求：这是重点！**必须**找出他"跨界"的优势。例如：懂Python的货运司机，比普通程序员更懂物流痛点；比普通司机更懂数据。这是他的降维打击能力。)
</p>

<p><strong>04. 具体的搞钱/破局战术 (Tactical Moves)</strong><br>
🎯 <strong>战术一：{TACTIC_1}</strong><br>
(要求：必须是一个**极小、极具体、明天就能做**的动作。例如：利用货运群的信息差接单，或者开发一个专门抓取"高价运单"的小脚本自己用。)<br>
<br>
🎯 <strong>战术二：{TACTIC_2}</strong><br>
(要求：必须结合内容创作。例如：拍摄"货车里的程序员"短视频，这个人设具备极强的反差感，必定火。)
</p>

<p class="encouragement">
<strong>❝ {INSPIRING_QUOTE} ❞</strong><br>
(给一句有力量的结语。)
</p>

【注意】
- **拒绝大词**：不要说"建立个人品牌"、"数字化转型"这种虚词。
- **要具体**：如果是货运司机，就建议他写脚本抢单、分析运费数据，或者做"最硬核的货运博主"。
- **要体谅**：承认他白天工作的辛苦，建议他用最小的精力撬动最大的杠杆。
- **评分标准**：{SCORE} 必须是 0-100 之间的整数（例如 85）。{RATING_LEVEL} 必须是 S, A, B, C, D 之一。
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