"""
generate_templates.py
Generates 16 GitHub README templates — 2 per category.
Every template uses ONLY standard placeholders from templateFields.ts.
Templates use <!-- SECTION:id --> markers so sections can be toggled.
All GIF/image URLs are hardcoded (no YOUR_GIF placeholders).
Run from project root: python generate_templates.py
"""

import os, textwrap

OUT = "md-templates"
os.makedirs(OUT, exist_ok=True)

# ── Standard placeholder reference (all resolve automatically) ────────────
# YOUR_USERNAME    YOUR_NAME        YOUR_TAGLINE     YOUR_ROLE
# YOUR_TITLE       YOUR_COMPANY     YOUR_FOCUS       YOUR_BIO
# YOUR_LOCATION    YOUR_CITY        YOUR_COUNTRY     YOUR_EMAIL
# YOUR_PROJECT     YOUR_LEARNING    YOUR_TOPICS      YOUR_TOOLS
# YOUR_TWITTER     YOUR_LINKEDIN    YOUR_WEBSITE     YOUR_YOUTUBE
# YOUR_QUOTE       YOUR_FUN_FACT    YOUR_GOAL
# YOUR_PROJECT_1   YOUR_PROJECT_2   YOUR_PROJECT_1_DESC  YOUR_PROJECT_2_DESC
# YOUR_PROJECT_1_DEMO  YOUR_PROJECT_2_DEMO
# YOUR_UNIVERSITY  YOUR_MAJOR       YOUR_YEAR        YOUR_YEARS
# YOUR_ACHIEVEMENT_1   YOUR_ACHIEVEMENT_2
# ─────────────────────────────────────────────────────────────────────────


def wrap(section_id: str, content: str) -> str:
    """Wrap content in section markers for toggling."""
    return f"<!-- SECTION:{section_id} -->\n{content.strip()}\n<!-- /SECTION:{section_id} -->"


# ══════════════════════════════════════════════════════════════════════════
# 1. MINIMAL — Clean & elegant
# ══════════════════════════════════════════════════════════════════════════

templates = {}

# ── 01: minimal-wave ─────────────────────────────────────────────────────
templates["01-minimal-wave.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=YOUR_NAME&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=YOUR_TAGLINE&descAlignY=55" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1000&color=58A6FF&center=true&vCenter=true&width=500&lines=Hi+there!+I'm+YOUR_NAME+👋;YOUR_ROLE;YOUR_TAGLINE" alt="Typing SVG"/>
</div>
"""),
    wrap("about", """
## 🧑‍💻 About Me

| | |
|:--|:--|
| 🔭 **Working on** | YOUR_PROJECT |
| 🌱 **Learning** | YOUR_LEARNING |
| 📍 **Location** | YOUR_CITY, YOUR_COUNTRY |
| 💼 **Role** | YOUR_ROLE |
| 📫 **Email** | YOUR_EMAIL |
| ⚡ **Fun fact** | YOUR_FUN_FACT |
"""),
    wrap("techStack", """
## 🛠 Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8" />
</p>
"""),
    wrap("githubStats", """
## 📊 GitHub Stats

<p align="center">
  <img height="160" src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=58A6FF&text_color=c9d1d9&icon_color=58A6FF"/>
  <img height="160" src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=transparent&hide_border=true&title_color=58A6FF&text_color=c9d1d9"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=transparent&hide_border=true&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=transparent&hide_border=true&title_color=58A6FF&text_color=c9d1d9"/>
</p>
"""),
    wrap("projects", """
## 🚀 Featured Projects

- **[YOUR_PROJECT_1](YOUR_PROJECT_1_DEMO)** — YOUR_PROJECT_1_DESC
- **[YOUR_PROJECT_2](YOUR_PROJECT_2_DEMO)** — YOUR_PROJECT_2_DESC
"""),
    wrap("socials", """
## 🤝 Connect With Me

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-FF7139?style=for-the-badge&logo=firefox-browser&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## ✨ Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=transparent&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=nord&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>
</div>
"""),
])

# ── 02: minimal-dark ─────────────────────────────────────────────────────
templates["02-minimal-dark.md"] = "\n\n".join([
    wrap("header", r"""
<div align="center">

```
 __   ______  _   _ _____     _   _    _    __  __ _____
 \ \ / / __ \| | | |  __ \   | \ | |  / \  |  \/  | ____|
  \ V / |  | | | | | |__) |  |  \| | / _ \ | |\/| |  _|
   | || |__| | |_| |  _  /   | |\  |/ ___ \| |  | | |___
   |_| \____/ \___/|_| \_\   |_| \_/_/   \_\_|  |_|_____|
```

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1000&color=00FF41&center=true&vCenter=true&width=600&lines=YOUR_ROLE;YOUR_TAGLINE;Building+YOUR_PROJECT" alt="Typing SVG"/>
</div>
"""),
    wrap("about", """
## 👤 About

```javascript
const dev = {
  name:     "YOUR_NAME",
  role:     "YOUR_ROLE",
  location: "YOUR_CITY, YOUR_COUNTRY",
  focus:    "YOUR_FOCUS",
  building: "YOUR_PROJECT",
  learning: "YOUR_LEARNING",
  email:    "YOUR_EMAIL",
};
```
"""),
    wrap("techStack", """
## ⚡ Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8&theme=dark"/>
</p>
"""),
    wrap("githubStats", """
## 📈 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dark&hide_border=true&bg_color=0d1117&title_color=00FF41&icon_color=00FF41&text_color=c9d1d9" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=00FF41&text_color=c9d1d9" height="160"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0d1117&ring=00FF41&fire=00FF41&currStreakLabel=00FF41" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🌐 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=dark&hide_border=true&bg_color=0d1117&title_color=00FF41&text_color=c9d1d9"/>
</p>
"""),
    wrap("projects", """
## 🔨 Projects

| Project | Description | Link |
|---------|-------------|------|
| YOUR_PROJECT_1 | YOUR_PROJECT_1_DESC | [View](YOUR_PROJECT_1_DEMO) |
| YOUR_PROJECT_2 | YOUR_PROJECT_2_DESC | [View](YOUR_PROJECT_2_DEMO) |
"""),
    wrap("socials", """
## 📡 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-000000?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 💬 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=darkhub&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=onedark&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
  <img src="https://komarev.com/ghpvc/?username=YOUR_USERNAME&style=flat-square&color=00FF41" alt="Profile views"/>
  <br/>
  <sub>Made with ❤️ by YOUR_NAME</sub>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# 2. ANIMATED — Dynamic & eye-catching
# ══════════════════════════════════════════════════════════════════════════

templates["03-animated-typing.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&animation=fadeIn&fontAlignY=38&fontAlign=50" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=F75C7E&center=true&vCenter=true&multiline=true&width=600&height=100&lines=Hi+there!+I'm+YOUR_NAME+👋;I'm+a+YOUR_ROLE;YOUR_TAGLINE" alt="Typing SVG"/>
<br/>
<img src="https://user-images.githubusercontent.com/74038190/235224431-e8c8c12e-6826-47f1-89fb-2ddad83b3abf.gif" width="300"/>
</div>
"""),
    wrap("about", """
## 🚀 About Me

- 🔭 Currently working on **YOUR_PROJECT**
- 🌱 Currently learning **YOUR_LEARNING**
- 🎯 Goal: **YOUR_GOAL**
- 📍 Based in **YOUR_CITY, YOUR_COUNTRY**
- 📫 Reach me at **YOUR_EMAIL**
- ⚡ Fun fact: **YOUR_FUN_FACT**
"""),
    wrap("techStack", """
## 🛠️ Technologies & Tools

<div align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</div>
"""),
    wrap("githubStats", """
## 📊 My GitHub Stats

<div align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" height="165"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=tokyonight&hide_border=true" height="165"/>
</div>
"""),
    wrap("streak", """
## 🔥 Streak Stats

<div align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=tokyonight&hide_border=true" width="60%"/>
</div>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<div align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=tokyonight&hide_border=true"/>
</div>
"""),
    wrap("projects", """
## 🧪 Featured Projects

<div align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=tokyonight&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=tokyonight&hide_border=true"/>
  </a>
</div>
"""),
    wrap("socials", """
## 🤝 Let's Connect!

<div align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox-browser&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</div>
"""),
    wrap("quote", """
## ✨ Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 GitHub Badges

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=tokyonight&no-frame=true&row=1&column=6"/>
</div>
"""),
    wrap("trophies", """
## 🏆 Trophies

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=tokyonight&no-frame=true&row=2&column=4"/>
</div>
"""),
    wrap("gifs", """
<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700"/>
</div>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>
<img src="https://komarev.com/ghpvc/?username=YOUR_USERNAME&style=for-the-badge&color=F75C7E" alt="Profile views"/>
</div>
"""),
])


templates["04-animated-neon.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=9,17,24&height=280&section=header&text=YOUR_NAME&fontSize=70&fontColor=00FFFF&animation=twinkling&fontAlignY=42&desc=YOUR_ROLE&descSize=22&descFontColor=FF00FF&descAlignY=63" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=18&pause=1000&color=00FFFF&center=true&vCenter=true&width=600&lines=YOUR_TAGLINE;Building+YOUR_PROJECT;Learning+YOUR_LEARNING" alt="Typing SVG"/>
<br/>
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400"/>
</div>
"""),
    wrap("about", """
## ⚡ About

```
╔══════════════════════════════════════╗
║  NAME     : YOUR_NAME               ║
║  ROLE     : YOUR_ROLE               ║
║  LOCATION : YOUR_CITY               ║
║  STATUS   : Building YOUR_PROJECT   ║
║  LEARNING : YOUR_LEARNING           ║
║  EMAIL    : YOUR_EMAIL              ║
╚══════════════════════════════════════╝
```
"""),
    wrap("techStack", """
## 🔧 Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8&theme=dark"/>
</p>
"""),
    wrap("githubStats", """
## 📡 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=00FFFF&icon_color=FF00FF&text_color=ffffff" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=00FFFF&text_color=ffffff" height="160"/>
</p>
"""),
    wrap("streak", """
## 💥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=radical&hide_border=true&background=0d0d0d&ring=00FFFF&fire=FF00FF&currStreakLabel=00FFFF" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🌐 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=00FFFF&text_color=ffffff"/>
</p>
"""),
    wrap("projects", """
## 🚀 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=00FFFF&text_color=ffffff"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=00FFFF&text_color=ffffff"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📡 Signal

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-00FFFF?style=for-the-badge&logo=twitter&logoColor=black"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FF00FF?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-00FFFF?style=for-the-badge&logo=gmail&logoColor=black"/></a>
</p>
"""),
    wrap("quote", """
## 🌌 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("gifs", """
<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212748830-4c709398-a386-4761-84d7-9e10b98fbe6e.gif" width="500"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=9,17,24&height=150&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# 3. FULL STACK
# ══════════════════════════════════════════════════════════════════════════

templates["05-fullstack-modern.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Full+Stack+Developer&descAlignY=60&descSize=22" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=22D3EE&center=true&vCenter=true&width=700&lines=Full+Stack+Developer+🚀;React+%2B+Node.js+%2B+Cloud+☁️;YOUR_TAGLINE" alt="Typing SVG"/>
<br/>
<img src="https://user-images.githubusercontent.com/74038190/229223156-0cbdaba9-3128-4d8e-8719-b6b4cf741b67.gif" width="400"/>
</div>
"""),
    wrap("about", """
## 🧑‍💻 About Me

<img align="right" src="https://user-images.githubusercontent.com/74038190/212748842-9fcbad5b-6173-4175-8a61-521f3dbb7514.gif" width="280"/>

- 🔭 Currently building **YOUR_PROJECT**
- 🌱 Mastering **YOUR_LEARNING**
- 🌍 Based in **YOUR_LOCATION**
- 💼 Role: **YOUR_ROLE**
- 🏢 At: **YOUR_COMPANY**
- 📫 Reach me at **YOUR_EMAIL**
- ⚡ **YOUR_FUN_FACT**

<br clear="right"/>
"""),
    wrap("techStack", """
## ⚙️ Tech Stack

### Frontend
<p>
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
</p>

### Backend & DevOps
<p>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 GitHub Stats

<div align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" height="165"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=tokyonight&hide_border=true" height="165"/>
</div>
"""),
    wrap("streak", """
## 🔥 Streak

<div align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=tokyonight&hide_border=true" width="55%"/>
</div>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<div align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=tokyonight&hide_border=true"/>
</div>
"""),
    wrap("projects", """
## 🏗️ Featured Projects

<div align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=tokyonight&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=tokyonight&hide_border=true"/>
  </a>
</div>
"""),
    wrap("socials", """
## 🌐 Connect

<div align="center">
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-22D3EE?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</div>
"""),
    wrap("quote", """
## 💬 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=tokyonight&no-frame=true&row=1&column=6"/>
</div>
"""),
    wrap("trophies", """
## 🏆 Trophies

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=tokyonight&no-frame=true&row=2&column=4"/>
</div>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12&height=100&section=footer" width="100%"/>
</div>
"""),
])


templates["06-fullstack-dashboard.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,20,14,5&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Full+Stack+Engineer&descAlignY=58" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=20&pause=2000&color=38BDF8&center=true&vCenter=true&width=600&lines=Frontend+%2B+Backend+%2B+Cloud+%3D+🚀;Building+products+people+love;YOUR_TAGLINE" alt="Dashboard Header"/>
</div>
"""),
    wrap("about", """
## 📋 Profile

| Field | Value |
|-------|-------|
| **Name** | YOUR_NAME |
| **Title** | YOUR_TITLE |
| **Location** | YOUR_LOCATION |
| **Company** | YOUR_COMPANY |
| **Status** | 🟢 Available |
| **Email** | YOUR_EMAIL |
"""),
    wrap("techStack", """
## 🏗️ Architecture Skills

| Layer | Technologies |
|-------|-------------|
| 🖥️ Frontend | YOUR_TOPICS |
| ⚙️ Backend & Tools | YOUR_TOOLS |
"""),
    wrap("githubStats", """
## 📊 Activity Dashboard

<div align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=github_dark&hide_border=true&count_private=true" height="165"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=github_dark&hide_border=true" height="165"/>
</div>
"""),
    wrap("streak", """
## 🔥 Streak

<div align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0f172a&ring=38BDF8&fire=38BDF8&currStreakLabel=38BDF8" width="55%"/>
</div>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<div align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=github_dark&hide_border=true"/>
</div>
"""),
    wrap("projects", """
## 🔗 Projects

<div align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=github_dark&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=github_dark&hide_border=true"/>
  </a>
</div>
"""),
    wrap("socials", """
## 🔗 Links

<div align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-38BDF8?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-0EA5E9?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-7C3AED?style=for-the-badge&logo=vercel&logoColor=white"/></a>
</div>
"""),
    wrap("quote", """
## 💡 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=darkhub&no-frame=true&row=1&column=6"/>
</div>
"""),
    wrap("trophies", """
## 🏆 Trophies

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=darkhub&no-frame=true&row=2&column=4"/>
</div>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,20,14,5&height=100&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# 4. STUDENT
# ══════════════════════════════════════════════════════════════════════════

templates["07-student-journey.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6,14&height=200&section=header&text=Hi!+I'm+YOUR_NAME+👋&fontSize=42&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Student+Developer+%40+YOUR_UNIVERSITY&descAlignY=60" width="100%"/>
<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="300"/>
<img src="https://readme-typing-svg.demolab.com?font=Nunito&size=20&pause=1000&color=34D399&center=true&vCenter=true&width=600&lines=Computer+Science+Student+🎓;Learning+to+code+one+bug+at+a+time+🐛;YOUR_TAGLINE" alt="Student Typing"/>
</div>
"""),
    wrap("about", """
## 📚 About Me

| | |
|:--|:--|
| 🎓 **School** | YOUR_UNIVERSITY |
| 📖 **Major** | YOUR_MAJOR |
| 📅 **Year** | YOUR_YEAR |
| 🔭 **Building** | YOUR_PROJECT |
| 🌱 **Learning** | YOUR_LEARNING |
| 🎯 **Goal** | YOUR_GOAL |
| ⚡ **Fun fact** | YOUR_FUN_FACT |
"""),
    wrap("skills", """
## 🌱 Skills So Far

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
</p>
"""),
    wrap("techStack", """
## 🛠 Current Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=vue&hide_border=true&count_private=true" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=vue&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=vue&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=vue&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🔨 Projects

- **[YOUR_PROJECT_1](YOUR_PROJECT_1_DEMO)** — YOUR_PROJECT_1_DESC
- **[YOUR_PROJECT_2](YOUR_PROJECT_2_DEMO)** — YOUR_PROJECT_2_DESC
"""),
    wrap("socials", """
## 🤝 Let's Connect!

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## ✨ Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=vue&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=algolia&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6,14&height=100&section=footer" width="100%"/>
</div>
"""),
])


templates["08-student-coder.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7,14,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=CS+Student+%40+YOUR_UNIVERSITY&descAlignY=60" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Source+Code+Pro&size=18&pause=1500&color=10B981&center=true&vCenter=true&width=600&lines=Learning+in+public+📖;Building+projects+🔨;Debugging+my+future+🐛;YOUR_TAGLINE" alt="Progress Typing"/>
</div>
"""),
    wrap("about", """
## 📊 Skill Progress

| Skill | Progress | Level |
|-------|----------|-------|
| YOUR_TECH_1 | `████████░░` 80% | Intermediate |
| YOUR_TECH_2 | `██████░░░░` 60% | Learning |
| Git | `███████░░░` 70% | Intermediate |
"""),
    wrap("skills", """
## 🛠 Learning Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
</p>
"""),
    wrap("techStack", """
## ⚙️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📈 GitHub Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=algolia&hide_border=true" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=algolia&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=algolia&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=algolia&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🔨 Projects

- **[YOUR_PROJECT_1](YOUR_PROJECT_1_DEMO)** — YOUR_PROJECT_1_DESC
- **[YOUR_PROJECT_2](YOUR_PROJECT_2_DEMO)** — YOUR_PROJECT_2_DESC
"""),
    wrap("socials", """
## 🌐 Connect

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-10B981?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-10B981?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=algolia&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=algolia&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7,14,20&height=100&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# 5. OPEN SOURCE
# ══════════════════════════════════════════════════════════════════════════

templates["09-opensource-contributor.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Open+Source+Contributor+🌟&descAlignY=60&descSize=20" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=FB923C&center=true&vCenter=true&width=700&lines=Open+source+is+my+playground+🌟;YOUR_ROLE;YOUR_TAGLINE" alt="OSS Typing"/>
</div>
"""),
    wrap("about", """
## 🌟 About

- 🔭 Working on **YOUR_PROJECT**
- 🌍 Based in **YOUR_LOCATION**
- 💼 **YOUR_ROLE** at **YOUR_COMPANY**
- 🌱 Learning **YOUR_LEARNING**
- 📫 Email: **YOUR_EMAIL**
- ⚡ **YOUR_FUN_FACT**
"""),
    wrap("techStack", """
## 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=github_dark&hide_border=true&count_private=true" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=github_dark&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=github-dark-blue&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=github_dark&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🔨 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=github_dark&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=github_dark&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🤝 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FB923C?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FB923C?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Blog-FB923C?style=for-the-badge&logo=hashnode&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 💬 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=gitdimmed&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=gitdimmed&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=100&section=footer" width="100%"/>
</div>
"""),
])


templates["10-opensource-maintainer.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:e96c4c,100:e96c4c&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=OSS+Maintainer+%7C+YOUR_ROLE&descAlignY=60" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=E96C4C&center=true&vCenter=true&width=700&lines=Maintaining+open+source+🔧;Code+reviews+are+an+act+of+love+❤️;YOUR_TAGLINE" alt="Maintainer Typing"/>
</div>
"""),
    wrap("about", """
## 🔧 About

```yaml
name:     YOUR_NAME
role:     YOUR_ROLE
company:  YOUR_COMPANY
location: YOUR_LOCATION
building: YOUR_PROJECT
learning: YOUR_LEARNING
email:    YOUR_EMAIL
```
"""),
    wrap("techStack", """
## 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=solarized-light&hide_border=true" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=solarized-light&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=solarized-light&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=solarized-light&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🔨 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=solarized-light&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=solarized-light&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📬 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-E96C4C?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-E96C4C?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:e96c4c,100:e96c4c&height=100&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# 6. DATA / AI
# ══════════════════════════════════════════════════════════════════════════

templates["11-data-ai-researcher.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,14,9&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=AI+%2F+ML+Engineer&descAlignY=60&descSize=20" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=18&pause=1000&color=818CF8&center=true&vCenter=true&width=700&lines=Pushing+the+frontiers+of+AI+🧠;YOUR_ROLE;YOUR_TAGLINE" alt="AI Typing"/>
<br/>
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100"/>
</div>
"""),
    wrap("about", """
## 🧪 About

- 🤖 Working on **YOUR_PROJECT**
- 🧠 Focus: **YOUR_FOCUS**
- 🌍 Based in **YOUR_LOCATION**
- 🌱 Learning **YOUR_LEARNING**
- 📫 Email: **YOUR_EMAIL**
- ⚡ **YOUR_FUN_FACT**
"""),
    wrap("techStack", """
## 🛠 Research Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dracula&hide_border=true" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dracula&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=dracula&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=dracula&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🔬 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=dracula&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=dracula&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🌐 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-818CF8?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-818CF8?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-818CF8?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 💬 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=dracula&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=dracula&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,14,9&height=100&section=footer" width="100%"/>
</div>
"""),
])


templates["12-data-ai-engineer.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,9&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=ML+Engineer&descAlignY=60&descSize=20" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=8B5CF6&center=true&vCenter=true&width=700&lines=Training+models+🤖;Deploying+AI+at+scale+🚀;YOUR_TAGLINE" alt="ML Typing"/>
</div>
"""),
    wrap("about", """
## 🤖 About

```python
class Engineer:
    name     = "YOUR_NAME"
    role     = "YOUR_ROLE"
    company  = "YOUR_COMPANY"
    location = "YOUR_LOCATION"
    building = "YOUR_PROJECT"
    learning = "YOUR_LEARNING"
    email    = "YOUR_EMAIL"
```
"""),
    wrap("techStack", """
## 🛠 ML Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=midnight-purple&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=midnight-purple&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=midnight-purple&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🔬 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=midnight-purple&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=midnight-purple&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🌐 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-8B5CF6?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-8B5CF6?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=midnight-purple&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=midnight-purple&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,9&height=100&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# 7. WEB3
# ══════════════════════════════════════════════════════════════════════════

templates["13-web3-defi.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Web3+%2F+DeFi+Developer&descAlignY=60" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=18&pause=1000&color=F59E0B&center=true&vCenter=true&width=700&lines=Building+decentralized+finance+🏦;YOUR_ROLE;YOUR_TAGLINE" alt="Web3 Typing"/>
<br/>
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100"/>
</div>
"""),
    wrap("about", """
## ⛓️ About

- 🔭 Building **YOUR_PROJECT**
- 🏢 At **YOUR_COMPANY**
- 🌍 Based in **YOUR_LOCATION**
- 🌱 Learning **YOUR_LEARNING**
- 📫 Email: **YOUR_EMAIL**
- ⚡ **YOUR_FUN_FACT**
"""),
    wrap("techStack", """
## 🛠 Blockchain Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=F59E0B&icon_color=F59E0B&text_color=d1d5db" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=F59E0B&text_color=d1d5db" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0d0d0d&ring=F59E0B&fire=F59E0B&currStreakLabel=F59E0B" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=F59E0B&text_color=d1d5db"/>
</p>
"""),
    wrap("projects", """
## 🔨 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=F59E0B&text_color=ffffff"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=F59E0B&text_color=ffffff"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📡 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-F59E0B?style=for-the-badge&logo=twitter&logoColor=black"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-F59E0B?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
</p>
"""),
    wrap("quote", """
> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=100&section=footer" width="100%"/>
</div>
"""),
])


templates["14-web3-solidity.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Solidity+Developer&descAlignY=60" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1000&color=627EEA&center=true&vCenter=true&width=700&lines=pragma+solidity+%5E0.8.0%3B;Building+trustless+systems+🔒;YOUR_TAGLINE" alt="Solidity Typing"/>
</div>
"""),
    wrap("about", """
## 🔒 About

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Developer {
    string public name     = "YOUR_NAME";
    string public role     = "YOUR_ROLE";
    string public location = "YOUR_LOCATION";
    string public building = "YOUR_PROJECT";
    string public learning = "YOUR_LEARNING";
}
```
"""),
    wrap("techStack", """
## ⛓️ Chain Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=ocean_dark&hide_border=true" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=ocean_dark&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=ocean-gradient&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=ocean_dark&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🔨 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=ocean_dark&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📡 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-627EEA?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-627EEA?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=ocean_dark&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=ocean_dark&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=100&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# 8. PROFESSIONAL
# ══════════════════════════════════════════════════════════════════════════

templates["15-professional-portfolio.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9&height=220&section=header&text=YOUR_NAME&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=YOUR_TITLE&descAlignY=60&descSize=24" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Lato&weight=700&size=20&pause=2000&color=0EA5E9&center=true&vCenter=true&width=700&lines=YOUR_TAGLINE;YOUR_ROLE+at+YOUR_COMPANY;Open+to+opportunities" alt="Professional Typing"/>
</div>
"""),
    wrap("about", """
## 💼 About

| | |
|:--|:--|
| 🏢 **Company** | YOUR_COMPANY |
| 💼 **Title** | YOUR_TITLE |
| 📍 **Location** | YOUR_LOCATION |
| 🔭 **Building** | YOUR_PROJECT |
| 🌱 **Learning** | YOUR_LEARNING |
| 📫 **Email** | YOUR_EMAIL |
"""),
    wrap("techStack", """
## 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=0EA5E9&icon_color=0EA5E9&text_color=94A3B8" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=transparent&hide_border=true&title_color=0EA5E9&text_color=94A3B8" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=transparent&hide_border=true&ring=0EA5E9&fire=0EA5E9&currStreakLabel=0EA5E9" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=transparent&hide_border=true&title_color=0EA5E9&text_color=94A3B8"/>
</p>
"""),
    wrap("projects", """
## 🚀 Featured Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=transparent&hide_border=true&title_color=0EA5E9&text_color=94A3B8"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=transparent&hide_border=true&title_color=0EA5E9&text_color=94A3B8"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📬 Contact

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-0EA5E9?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Hire+Me-10B981?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 💬 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=nord&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=nord&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9&height=100&section=footer" width="100%"/>
</div>
"""),
])


templates["16-professional-recruiter.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,14&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=YOUR_TITLE+%7C+YOUR_COMPANY&descAlignY=60&descSize=20" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Raleway&weight=600&size=20&pause=2000&color=3B82F6&center=true&vCenter=true&width=700&lines=YOUR_YEARS%2B+years+of+experience+💼;YOUR_ROLE;YOUR_TAGLINE" alt="Recruiter Typing"/>
</div>
"""),
    wrap("about", """
## 📋 Professional Summary

YOUR_BIO

- 🏢 **Company:** YOUR_COMPANY
- 💼 **Role:** YOUR_ROLE
- 📍 **Location:** YOUR_LOCATION
- 🎓 **Education:** YOUR_MAJOR, YOUR_UNIVERSITY
- 📫 **Email:** YOUR_EMAIL
"""),
    wrap("techStack", """
## 🛠 Core Competencies

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 GitHub Activity

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=default&hide_border=false&title_color=3B82F6&icon_color=3B82F6" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=default&hide_border=false" height="155"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=default&hide_border=false&ring=3B82F6&fire=3B82F6&currStreakLabel=3B82F6" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=default&hide_border=false"/>
</p>
"""),
    wrap("projects", """
## 🚀 Key Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=default&hide_border=false"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=default&hide_border=false"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📬 Contact

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-3B82F6?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 💬 Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=flat&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=flat&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,14&height=100&section=footer" width="100%"/>
</div>
"""),
])


# ── Write all files ───────────────────────────────────────────────────────
for filename, content in templates.items():
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print(f"Generated {len(templates)} templates in ./{OUT}/")
for name in sorted(templates.keys()):
    print(f"  • {name}")