import streamlit as st
from openai import OpenAI
import auth

# ==========================================
# 1. 页面配置
# ==========================================
st.set_page_config(
    page_title="赛博·财富架构师",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. 样式定义 (CSS 写死在这里，最稳)
# ==========================================
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #0E1117; }
    
    /* 核心卡片样式 */
    .cyber-card {
        background-color: #000000;
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 25px;
        color: #E0E0E0;
        font-family: sans-serif;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.15);
        margin-top: 20px;
    }
    .cyber-title {
        color: #FFD700;
        font-size: 24px;
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
    }
    .cyber-subtitle {
        color: #666;
        font-size: 12px;
        text-align: center;
        margin-bottom: 20px;
        border-bottom: 1px dashed #333;
        padding-bottom: 10px;
    }
    .cyber-score {
        display: block;
        margin: 10px auto;
        border: 3px solid #FF4500;
        color: #FF4500;
        padding: 10px 20px;
        font-size: 36px;
        font-weight: 900;
        transform: rotate(-3deg);
        border-radius: 10px;
        text-align: center;
        width: fit-content;
        font-family: impact, sans-serif;
    }
    .cyber-section {
        color: #00BFFF;
        font-weight: bold;
        font-size: 18px;
        margin-top: 25px;
        margin-bottom: 10px;
        border-left: 4px solid #00BFFF;
        padding-left: 10px;
    }
    .cyber-highlight {
        color: #FFD700;
        font-weight: bold;
    }
    .cyber-quote {
        margin-top: 30px;
        padding: 15px;
        background-color: #0f1a0f;
        border-left: 4px solid #00FF00;
        color: #98fb98;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 统一发卡机验证逻辑 (无变化)
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/3d-fluency/94/money-bag-bitcoin.png", width=60)
    st.markdown("### 🔐 身份验证")
    
    if "license_verified" not in st.session_state:
        st.session_state.license_verified = False
        st.session_state.card_type = ""

    if not st.session_state.license_verified:
        st.info("🔒 系统已加密，请获取卡密解锁")
        st.markdown("💰 **单次清醒卡：9.9元**")
        st.markdown("👑 **长期军师卡：39元**")
        st.markdown("---")
        
        input_key = st.text_input("请输入【赛博通行证】", type="password")
        st.markdown("(客服微信: liao13689209126)")
        
        if st.button("激活系统", type="primary"):
            with st.spinner("☁️ 正在连接赛博矩阵云端..."):
                is_valid, msg, card_type = auth.check_license(input_key, 'fortune')
                if is_valid:
                    st.session_state.license_verified = True
                    st.session_state.card_type = card_type
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)
    else:
        st.success(f"已激活: {st.session_state.card_type}")
        if st.button("退出登录"):
            st.session_state.license_verified = False
            st.rerun()

    st.markdown("---")
    st.caption("🤖 Powered by DeepSeek-V3")

# ==========================================
# 4. 拦截逻辑 (无变化)
# ==========================================
if not st.session_state.license_verified:
    st.title("💸 赛博·财富架构师")
    st.markdown("---")
    st.markdown("### 👁️ 为什么要测？")
    st.image("case_study.png", caption="真实案例：挽回50万止损", width="stretch") 
    st.info("💡 这是一个基于博弈论和概率学的商业决策评估系统。")
    st.markdown("### 🔓 立即解锁算力")
    with st.container():
        st.warning("🔥 限时体验：**9.9元** / 24小时")
        with st.expander("👉 点击获取【财富通行证】(微信/支付宝)", expanded=False):
            st.write("1. 扫码支付 9.9 元")
            col1, col2 = st.columns(2)
            with col1:
                st.image("pay_wechat.png", caption="微信支付")
            with col2:
                st.image("pay_alipay.png", caption="支付宝支付")
            st.write("2. 支付备注 **【财神】**")
            st.write("3. 截图发给客服，秒发通行证密码")
    st.text_input("请输入【赛博通行证】", placeholder="请先在侧边栏或上方解锁...", disabled=True)
    st.button("激活系统", disabled=True)
    st.stop()

# ==========================================
# 5. 核心功能：DeepSeek 接入
# ==========================================
try:
    API_KEY = st.secrets["DEEPSEEK_API_KEY"]
    BASE_URL = "https://api.deepseek.com"
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
except:
    st.error("⚠️ 未配置 API Key")
    st.stop()

# ★★★★★ 核心 Prompt 简化版：只负责填空 ★★★★★
SYSTEM_PROMPT = """
你是一位【赛博人生架构师】。
【重要指令：渲染模式】
你现在的身份不是聊天助手，而是一个 **无头(Headless) API 端点**。
你的输出将被直接传送给前端渲染引擎 (`st.markdown(unsafe_allow_html=True)`)。

【思维逻辑链】
1. 分析用户输入。
2. 在内心构建赛博朋克风格的分析报告。
3. **关键判断**：如果输出包含 ` ```html ` 或 `**` 等 Markdown 标记，前端会渲染失败，显示为乱码。
4. **执行结果**：因此，我必须输出 **纯净的 HTML 字符串**。

【输出要求】
- **起始字符**必须是 `<div`。
- **结束字符**必须是 `</div>`。
- **严禁**使用 Markdown 代码块标记。
- **严禁**使用 Markdown 加粗符号。
- 高亮重点请直接使用 `<span style='color: #FFD700; font-weight: bold;'>内容</span>`。
- **必须根据用户输入生成实际内容，不要使用模板中的示例文字！**

【HTML 结构说明】（仅供参考，不要输出这些文字）
你需要生成以下结构的 HTML：
1. 外层容器：`<div class="cyber-card">`
2. 标题：`<div class="cyber-title">` - 显示 "🚀 赛博突围报告"
3. 副标题：`<div class="cyber-subtitle">` - 显示 "BREAKTHROUGH STRATEGY"
4. 评分：`<div class="cyber-score">` - 显示评分和等级（如 "85分 / S级"）
5. 四个章节，每个章节使用 `<div class="cyber-section">` 作为标题：
   - 01. 局势透视 (Reality Check)
   - 02. 导师直言 (The Truth)
   - 03. 你的独家优势 (The X-Factor)
   - 04. 具体的搞钱/破局战术 (Tactical Moves)
6. 鼓励语：`<div class="cyber-quote">` - 显示一句激励的话

【内容生成规则】
- 评分：根据用户情况给出 0-100 分和等级（S/A/B/C）
- 局势透视：分析用户的生存现状、核心矛盾、潜在爆发力
- 导师直言：给出直接、犀利的评价
- 独家优势：找出用户的独特优势
- 战术：给出 2 个具体的、可执行的战术建议
- 鼓励语：一句激励的话

【重要提醒】
- 上面的"结构说明"只是告诉你需要生成什么样的 HTML，不要把这些说明文字输出！
- 必须根据用户输入生成实际内容，不要复制任何示例文字！
- 只输出最终的 HTML 代码，从 `<div class="cyber-card">` 开始，到 `</div>` 结束
"""

st.title("💸 赛博·财富架构师")
if st.session_state.card_type:
    st.caption(f"当前身份: {st.session_state.card_type} | 🟢 算力全开")

user_query = st.text_area(
    "输入您的决策计划 (Project Protocol)", 
    height=150, 
    placeholder="例如：我是一名货车司机，自学了Python，想知道除了接单外包，还有什么利用这个技能搞钱的路子？"
)

if st.button("🚀 启动推演 (RUN SIMULATION)", type="primary"):
    if not user_query:
        st.warning("⚠️ 请输入您的计划")
    else:
        with st.spinner("🔄 正在加载高维商业模型..."):
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
                
                content = response.choices[0].message.content
                # 再次清洗，确保万无一失
                content = content.replace("```html", "").replace("```", "").strip()
                
                st.markdown(content, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ 错误: {e}")

st.markdown("<br><br>", unsafe_allow_html=True)