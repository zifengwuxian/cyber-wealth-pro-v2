# 赛博·财富架构师

> "世间无运气，一切皆概率。" - 基于高维金融算法的智能商业决策评估系统

## 📋 项目简介

赛博·财富架构师是一款基于 DeepSeek AI 的智能决策评估工具，通过毒舌而专业的风格，为用户提供绝对理性的商业决策评估。系统采用黑金高端UI设计，支持移动端完美适配，帮助用户在创业、投资、职业规划等方面做出更明智的决策。

## ✨ 核心功能

### 1. 智能决策评估
- 基于 DeepSeek-V3 大语言模型
- 毒舌点评风格，一针见血
- 量化评分系统（S/A/B/C/D 五级评级）
- 包含胜率、赔率、破产概率等金融指标

### 2. 完整评估报告
- 核心算法解析（Algorithm Analysis）
- 毒舌点评（Critical Review）
- 风险扫描（Black Swan Scan）
- 优化/止损建议（Action Items）

### 3. 云端验证系统
- 基于 GitHub Gist 的云端数据库
- 支持多应用卡密管理
- 实时验证，安全可靠
- 支持体验卡、月卡、全家桶等多种套餐

### 4. 移动端优先设计
- 响应式布局，完美适配手机端
- 三明治结构，优化用户浏览流程
- 隐藏开发工具UI，呈现原生App体验
- 支付码折叠保护，避免平台封号

## 🎨 界面特色

### 黑金高端风格
- 彭博终端风格配色
- 金色按钮与输入框
- 印章式评分展示
- 流畅的动画效果

### 视觉冲击力设计
- 3.5em 大号评分印章
- Impact 字体，-5度倾斜
- 边框与发光效果
- 手机端自动适配（2.5em）

## 🛠️ 技术栈

- **前端框架**: Streamlit 1.54.0
- **AI模型**: DeepSeek-V3 (OpenAI API)
- **数据存储**: GitHub Gist (云端数据库)
- **验证系统**: Python requests + JSON
- **样式设计**: CSS3 + 响应式媒体查询

## 📦 安装部署

### 环境要求
- Python 3.11+
- pip 包管理器

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd cyber-wealth
```

2. **创建虚拟环境**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **配置密钥**

创建 `.streamlit/secrets.toml` 文件：
```toml
GITHUB_TOKEN = "your_github_token"
GIST_ID = "your_gist_id"
DEEPSEEK_API_KEY = "your_deepseek_api_key"
```

5. **启动应用**
```bash
streamlit run app.py
```

访问 http://localhost:8501

## 💰 套餐定价

### 体验卡
- **价格**: 9.9元
- **时长**: 24小时
- **功能**: 无限次评估
- **适用**: 临时体验用户

### 长期军师卡
- **价格**: 39元
- **时长**: 30天
- **功能**: 无限次评估
- **适用**: 创业者、多项目用户

### 紫蜂矩阵·至尊全家桶
- **价格**: 99元
- **时长**: 一年
- **功能**: 解锁所有应用（财神+公文+外贸+爆款机+永久更新）
- **适用**: 长期用户、团队协作

## 🔐 验证系统说明

### 卡密类型
- **ADMIN-MASTER-001**: 管理员至尊卡，全应用访问权限
- **FORTUNE-xxxxx**: 财富架构师专用卡
- **ALL-xxxxx**: 全家桶卡，所有应用通用

### 验证流程
1. 用户在侧边栏输入卡密
2. 系统连接 GitHub Gist 云端数据库
3. 验证卡密有效性和适用范围
4. 激活成功，解锁完整功能

### 安全特性
- 云端实时验证
- 卡密绑定设备（可选）
- 状态管理（UNUSED/ACTIVE/BANNED）
- 应用范围控制

## 📱 使用指南

### 首次使用
1. 访问应用地址
2. 查看真实案例截图（钩子）
3. 点击展开支付码
4. 扫码支付获取卡密
5. 输入卡密激活系统

### 生成评估报告
1. 在输入框中描述你的决策计划
2. 点击"RUN SIMULATION"启动推演
3. 等待 AI 分析（约3-5秒）
4. 查看完整评估报告
5. 根据建议优化决策

### 报告解读
- **S级 (90-100分)**: 优秀方案，风险可控
- **A级 (80-89分)**: 良好方案，需微调
- **B级 (70-79分)**: 一般方案，有风险
- **C级 (60-69分)**: 较差方案，需重构
- **D级 (0-59分)**: 危险方案，立即止损

## 🎯 最佳实践

### 输入建议
- 详细描述项目背景
- 包含资金规模和时间线
- 说明预期收益和风险承受能力
- 提供具体执行步骤

### 报告使用
- 重点关注"毒舌点评"部分
- 认真阅读"风险扫描"
- 执行"优化/止损建议"
- 结合AI建议调整方案

### 付费建议
- 体验卡适合单次评估
- 长期卡适合多项目评估
- 全家桶适合团队协作

## 🔧 配置说明

### secrets.toml 配置项
```toml
# GitHub API 配置
GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxx"
GIST_ID = "1af00d503d39014b974d3d6d52076624"

# DeepSeek API 配置
DEEPSEEK_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxx"

# 可选：智谱AI配置
ZHIPU_KEY = "xxxxxxxxxxxxxxxxxxxxxxxx.CfeNn6zyxDWM0Ie9"
```

### 图片资源
- `pay_wechat.png`: 微信支付二维码
- `pay_alipay.png`: 支付宝支付二维码
- `货拉拉+交易.png`: 真实案例展示图

## 🚀 部署到生产环境

### Streamlit Cloud 部署
1. 将代码推送到 GitHub
2. 访问 [share.streamlit.io](https://share.streamlit.io)
3. 连接 GitHub 仓库
4. 自动部署完成

### 自建服务器部署
```bash
# 使用 systemd 服务
sudo nano /etc/systemd/system/cyber-wealth.service
```

```ini
[Unit]
Description=Cyber Wealth Streamlit App
After=network.target

[Service]
User=your_user
WorkingDirectory=/path/to/cyber-wealth
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/streamlit run app.py --server.port 8501

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable cyber-wealth
sudo systemctl start cyber-wealth
```

## ❓ 常见问题

### Q1: 卡密验证失败怎么办？
A: 请检查：
- 卡密是否输入正确
- 卡密是否适用于当前应用
- 网络连接是否正常
- GitHub Token 是否有效

### Q2: AI 评估不准确怎么办？
A: 评估基于概率论和行为经济学，建议：
- 提供更详细的项目信息
- 明确风险承受能力
- 结合实际情况综合判断

### Q3: 支付后未收到卡密？
A: 请：
- 确认支付成功
- 联系客服微信：liao13689209126
- 提供支付截图

### Q4: 手机端显示异常？
A: 本项目已优化移动端适配：
- 使用竖屏浏览体验最佳
- 建议使用 Chrome 或 Safari 浏览器
- 清除缓存后重试

### Q5: 如何获取管理员权限？
A: 联系开发者获取 ADMIN-MASTER-001 卡密

## 📞 技术支持

- **客服微信**: liao13689209126
- **问题反馈**: GitHub Issues
- **更新日志**: 查看项目 README 更新

## 📄 许可证

本项目仅供学习和个人使用，商业使用请联系作者。

## 🙏 致谢

感谢以下开源项目和技术支持：
- Streamlit - Web应用框架
- DeepSeek - AI语言模型
- GitHub - 代码托管与数据存储

---

**赛博·财富架构师** - 让每一次决策都经过理性推演 💸
