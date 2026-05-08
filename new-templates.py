"""
generate_more_templates.py
Generates 24 additional GitHub README templates (templates 17-40).
Same placeholders & URL structure as existing templates.
New visual styles: space, cyberpunk, pastel, forest, ocean, sunset, hacker, galaxy, etc.
Run from project root: python generate_more_templates.py
"""

import os

OUT = "md-templates"
os.makedirs(OUT, exist_ok=True)

def wrap(section_id: str, content: str) -> str:
    return f"<!-- SECTION:{section_id} -->\n{content.strip()}\n<!-- /SECTION:{section_id} -->"

# ── GIF library (all from github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub) ─
GIFS = {
    "coding":    "https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif",
    "rocket":    "https://user-images.githubusercontent.com/74038190/216644497-1951db19-8f3d-4e44-ac08-8e9d7e0d94a7.gif",
    "wave":      "https://user-images.githubusercontent.com/74038190/235224431-e8c8c12e-6826-47f1-89fb-2ddad83b3abf.gif",
    "matrix":    "https://user-images.githubusercontent.com/74038190/212284119-fbfd994d-8c2a-4a07-a75f-84e513833c1c.gif",
    "snake":     "https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif",
    "robot":     "https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif",
    "globe":     "https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif",
    "laptop":    "https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif",
    "fire":      "https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif",
    "stars":     "https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif",
    "typing":    "https://user-images.githubusercontent.com/74038190/212748842-9fcbad5b-6173-4175-8a61-521f3dbb7514.gif",
    "neon":      "https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif",
    "circuit":   "https://user-images.githubusercontent.com/74038190/212748830-4c709398-a386-4761-84d7-9e10b98fbe6e.gif",
    "space":     "https://user-images.githubusercontent.com/74038190/216649426-0c2ee152-84d8-4707-85c4-27a378d2f78a.gif",
    "hack":      "https://user-images.githubusercontent.com/74038190/216644497-1951db19-8f3d-4e44-ac08-8e9d7e0d94a7.gif",
    "cat":       "https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif",
    "div_bar":   "https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif",
}

templates = {}

# ══════════════════════════════════════════════════════════════════════════
# SPACE / GALAXY THEME
# ══════════════════════════════════════════════════════════════════════════

templates["17-space-explorer.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=galaxy&color=gradient&height=280&section=header&text=YOUR_NAME&fontSize=65&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Exploring+the+universe+of+code+🚀&descAlignY=62&descSize=18" width="100%"/>

<img src="{GIFS['space']}" width="200"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=18&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=🌌+Exploring+the+cosmos+of+code;🚀+YOUR_ROLE;⭐+YOUR_TAGLINE;🪐+Building+YOUR_PROJECT" alt="Space Typing"/>
</div>
"""),
    wrap("about", """
## 🌟 Mission Control

```
╔═══════════════════════════════════════════╗
║  🚀 ASTRONAUT  : YOUR_NAME               ║
║  🎯 MISSION    : YOUR_PROJECT            ║
║  📡 SECTOR     : YOUR_LOCATION           ║
║  🛸 ROLE       : YOUR_ROLE               ║
║  🌱 STUDYING   : YOUR_LEARNING           ║
║  📧 SIGNAL     : YOUR_EMAIL              ║
║  ⚡ FUN FACT   : YOUR_FUN_FACT           ║
╚═══════════════════════════════════════════╝
```
"""),
    wrap("techStack", """
## 🛸 Fleet Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", f"""
## 📡 Mission Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true&bg_color=0d0d2b&title_color=A78BFA&icon_color=A78BFA&text_color=c9d1d9" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=midnight-purple&hide_border=true&bg_color=0d0d2b&title_color=A78BFA&text_color=c9d1d9" height="160"/>
</p>

<img src="{GIFS['stars']}" width="900"/>
"""),
    wrap("streak", """
## 🌠 Launch Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=midnight-purple&hide_border=true&background=0d0d2b&ring=A78BFA&fire=A78BFA&currStreakLabel=A78BFA" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🌌 Language Galaxy

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=midnight-purple&hide_border=true&bg_color=0d0d2b&title_color=A78BFA&text_color=c9d1d9"/>
</p>
"""),
    wrap("projects", f"""
## 🛰️ Space Missions

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=midnight-purple&hide_border=true&bg_color=0d0d2b&title_color=A78BFA&text_color=c9d1d9"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=midnight-purple&hide_border=true&bg_color=0d0d2b&title_color=A78BFA&text_color=c9d1d9"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📡 Open Transmission

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-A78BFA?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-A78BFA?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-7C3AED?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 🌌 Transmission

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Achievements

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=algolia&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Hall of Stars

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=darkhub&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("gifs", f"""
<div align="center">
  <img src="{GIFS['rocket']}" width="200"/>
</div>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=galaxy&color=gradient&height=150&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# CYBERPUNK THEME
# ══════════════════════════════════════════════════════════════════════════

templates["18-cyberpunk-hacker.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,100:FF2D78&height=4" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=40&pause=500&color=FF2D78&center=true&vCenter=true&width=700&lines=SYSTEM+BOOT...;IDENTITY+CONFIRMED;%3E+YOUR_NAME;%3E+YOUR_ROLE;HACK+THE+PLANET+💀" alt="Cyberpunk Boot"/>

<img src="{GIFS['neon']}" width="500"/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:FF2D78,100:000000&height=4" width="100%"/>
</div>
"""),
    wrap("about", """
## 🔴 PROFILE.EXE

```
┌─────────────────────────────────────────────────┐
│  > whoami                                        │
│                                                  │
│  NAME     >>  YOUR_NAME                         │
│  ALIAS    >>  YOUR_ROLE                         │
│  GRID     >>  YOUR_CITY                         │
│  CORP     >>  YOUR_COMPANY                      │
│  JOB      >>  YOUR_PROJECT                      │
│  UPLINK   >>  YOUR_EMAIL                        │
│  STATUS   >>  [ONLINE] 🟢                       │
│                                                  │
│  > _                                             │
└─────────────────────────────────────────────────┘
```
"""),
    wrap("techStack", f"""
## ⚡ WEAPONS CACHE

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8&theme=dark"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8&theme=dark"/>
</p>

<img src="{GIFS['circuit']}" width="700"/>
"""),
    wrap("githubStats", """
## 📊 NET METRICS

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical&hide_border=true&bg_color=0a0a0a&title_color=FF2D78&icon_color=FF2D78&text_color=ff9a9a" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=radical&hide_border=true&bg_color=0a0a0a&title_color=FF2D78&text_color=ff9a9a" height="160"/>
</p>
"""),
    wrap("streak", """
## 🔥 UPTIME

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=radical&hide_border=true&background=0a0a0a&ring=FF2D78&fire=FF0000&currStreakLabel=FF2D78" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💻 LANGUAGE MATRIX

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=radical&hide_border=true&bg_color=0a0a0a&title_color=FF2D78&text_color=ff9a9a"/>
</p>
"""),
    wrap("projects", """
## 🔌 ACTIVE PROGRAMS

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=radical&hide_border=true&bg_color=0a0a0a&title_color=FF2D78&text_color=ffffff"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=radical&hide_border=true&bg_color=0a0a0a&title_color=FF2D78&text_color=ffffff"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📡 UPLINK CHANNELS

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FF2D78?style=for-the-badge&logo=twitter&logoColor=black"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FF2D78?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-FF2D78?style=for-the-badge&logo=gmail&logoColor=black"/></a>
</p>
"""),
    wrap("quote", """
## 💬 BROADCAST

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 ACHIEVEMENTS UNLOCKED

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 TROPHY ROOM

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("gifs", f"""
<div align="center">
  <img src="{GIFS['matrix']}" width="600"/>
</div>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:FF2D78,100:000000&height=4" width="100%"/>
<br/>
<sub>⚡ SYSTEM UPTIME: ALWAYS | YOUR_NAME.exe</sub>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# PASTEL / SOFT THEME
# ══════════════════════════════════════════════════════════════════════════

templates["19-pastel-soft.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=0,2,2,5,30&height=200&section=header&text=Hello!+I'm+YOUR_NAME+🌸&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=YOUR_TAGLINE&descAlignY=62" width="100%"/>

<img src="{GIFS['cat']}" width="120"/>

<img src="https://readme-typing-svg.demolab.com?font=Nunito&size=20&pause=1000&color=FF6B9D&center=true&vCenter=true&width=600&lines=Passionate+about+clean+code+🌟;YOUR_ROLE+✨;YOUR_TAGLINE+🌸;Building+YOUR_PROJECT+💻" alt="Pastel Typing"/>
</div>
"""),
    wrap("about", """
## 🌷 About Me

```
 ♡ Name      : YOUR_NAME
 ♡ Role      : YOUR_ROLE
 ♡ Location  : YOUR_CITY, YOUR_COUNTRY
 ♡ Company   : YOUR_COMPANY
 ♡ Building  : YOUR_PROJECT
 ♡ Learning  : YOUR_LEARNING
 ♡ Goal      : YOUR_GOAL
 ♡ Fun Fact  : YOUR_FUN_FACT
 ♡ Email     : YOUR_EMAIL
```
"""),
    wrap("techStack", f"""
## 🎀 My Tech Palette

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>

<img src="{GIFS['coding']}" width="400"/>
"""),
    wrap("githubStats", """
## 📊 GitHub Garden

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=rose_pine&hide_border=true" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=rose_pine&hide_border=true" height="160"/>
</p>
"""),
    wrap("streak", """
## 🌸 Bloom Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=rose_pine&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🌺 Language Garden

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=rose_pine&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🌼 My Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=rose_pine&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=rose_pine&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🌸 Let's Chat!

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FF6B9D?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FF6B9D?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-FF6B9D?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-FF6B9D?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 🌟 Inspiration

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=discord&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=discord&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# OCEAN / AQUA THEME
# ══════════════════════════════════════════════════════════════════════════

templates["20-ocean-depths.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:006994,100:00D4FF&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=38&desc=YOUR_ROLE+🌊&descAlignY=62" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=Diving+deep+into+code+🌊;YOUR_ROLE;YOUR_TAGLINE;Building+YOUR_PROJECT" alt="Ocean Typing"/>

<img src="{GIFS['globe']}" width="150"/>
</div>
"""),
    wrap("about", """
## 🐠 About Me

<table>
<tr>
<td>

🌊 **Exploring:** YOUR_PROJECT  
🐚 **Based in:** YOUR_CITY, YOUR_COUNTRY  
💼 **Role:** YOUR_ROLE  
🐟 **Company:** YOUR_COMPANY  
🌱 **Learning:** YOUR_LEARNING  
📧 **Email:** YOUR_EMAIL  
⚡ **Fun fact:** YOUR_FUN_FACT  

</td>
<td>

<img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=ocean_dark&hide_border=true" height="175"/>

</td>
</tr>
</table>
"""),
    wrap("techStack", """
## 🔱 Deep Sea Toolkit

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Ocean Metrics

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=ocean_dark&hide_border=true" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=ocean_dark&hide_border=true" height="160"/>
</p>
"""),
    wrap("streak", """
## 🌊 Tide Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=ocean-gradient&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🐙 Language Reef

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=ocean_dark&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🚢 Fleet

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=ocean_dark&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=ocean_dark&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🐋 Connections

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-006994?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-00D4FF?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-006994?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-00D4FF?style=for-the-badge&logo=gmail&logoColor=black"/></a>
</p>
"""),
    wrap("quote", """
## 💬 Message in a Bottle

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=matrix&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=matrix&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:006994,100:00D4FF&height=120&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# SUNSET / GRADIENT THEME
# ══════════════════════════════════════════════════════════════════════════

templates["21-sunset-vibes.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3a1c71,50:d76d77,100:ffaf7b&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=YOUR_TAGLINE&descAlignY=62&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Pacifico&size=24&pause=1200&color=d76d77&center=true&vCenter=true&width=700&lines=Creative+Developer+🎨;YOUR_ROLE+✨;YOUR_TAGLINE;Building+YOUR_PROJECT+🔥" alt="Sunset Typing"/>

<img src="{GIFS['wave']}" width="300"/>
</div>
"""),
    wrap("about", """
## 🌅 About Me

- 🔭 Currently working on **YOUR_PROJECT**
- 🌱 Currently learning **YOUR_LEARNING**
- 💼 **YOUR_ROLE** at **YOUR_COMPANY**
- 🎯 Goal: **YOUR_GOAL**
- 📍 Based in **YOUR_CITY, YOUR_COUNTRY**
- 📫 Reach me: **YOUR_EMAIL**
- ⚡ Fun fact: **YOUR_FUN_FACT**
"""),
    wrap("techStack", """
## 🎨 Creative Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Sunset Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=sunset-gradient&hide_border=true" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=sunset-gradient&hide_border=true" height="160"/>
</p>
"""),
    wrap("streak", """
## 🔥 Golden Hour Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=sunset-gradient&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🌇 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=sunset-gradient&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🌆 Showcase

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=sunset-gradient&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=sunset-gradient&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🌸 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-d76d77?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-3a1c71?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-ffaf7b?style=for-the-badge&logo=google-chrome&logoColor=black"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-d76d77?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## ☀️ Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Badges

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=discord&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=discord&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3a1c71,50:d76d77,100:ffaf7b&height=120&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# FOREST / NATURE THEME
# ══════════════════════════════════════════════════════════════════════════

templates["22-forest-coder.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:1B4332,100:52B788&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=YOUR_ROLE+🌿&descAlignY=62" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Ubuntu&size=20&pause=1200&color=52B788&center=true&vCenter=true&width=700&lines=Growing+through+code+🌱;YOUR_ROLE;YOUR_TAGLINE;Planting+seeds+in+YOUR_PROJECT" alt="Forest Typing"/>
</div>
"""),
    wrap("about", """
## 🌿 About Me

```yaml
# about.yml
name: YOUR_NAME
role: YOUR_ROLE
company: YOUR_COMPANY
location: YOUR_CITY, YOUR_COUNTRY
currently_building: YOUR_PROJECT
currently_learning: YOUR_LEARNING
goal: YOUR_GOAL
email: YOUR_EMAIL
fun_fact: YOUR_FUN_FACT
```
"""),
    wrap("techStack", """
## 🌲 Tech Forest

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Growth Rings

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=vue&hide_border=true&title_color=52B788&icon_color=52B788" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=vue&hide_border=true&title_color=52B788" height="160"/>
</p>
"""),
    wrap("streak", """
## 🌱 Seedling Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=vue&hide_border=true&ring=52B788&fire=52B788&currStreakLabel=52B788" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🍃 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=vue&hide_border=true&title_color=52B788"/>
</p>
"""),
    wrap("projects", """
## 🌳 Projects in Bloom

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=vue&hide_border=true&title_color=52B788"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=vue&hide_border=true&title_color=52B788"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🌾 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-52B788?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-1B4332?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-52B788?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-1B4332?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 🍀 Quote

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
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:1B4332,100:52B788&height=120&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# FIRE / ORANGE ENERGY THEME
# ══════════════════════════════════════════════════════════════════════════

templates["23-fire-energy.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5,2,1&height=220&section=header&text=YOUR_NAME&fontSize=60&fontColor=fff&animation=twinkling&fontAlignY=38&desc=YOUR_ROLE&descAlignY=60" width="100%"/>

<img src="{GIFS['fire']}" width="100"/>

<img src="https://readme-typing-svg.demolab.com?font=Bebas+Neue&size=32&pause=800&color=FF6B35&center=true&vCenter=true&width=600&lines=ON+FIRE+WITH+CODE+🔥;YOUR_ROLE;YOUR_TAGLINE;BUILDING+THE+FUTURE" alt="Fire Typing"/>
</div>
"""),
    wrap("about", """
## ⚡ About Me

- 🔥 Working on: **YOUR_PROJECT**
- 💥 Speciality: **YOUR_FOCUS**
- 🌍 Based in: **YOUR_LOCATION**
- 🏢 At: **YOUR_COMPANY**
- 📚 Learning: **YOUR_LEARNING**
- 🎯 Goal: **YOUR_GOAL**
- 📧 Email: **YOUR_EMAIL**
- ⚡ Fun Fact: **YOUR_FUN_FACT**
"""),
    wrap("techStack", f"""
## 🔥 Blazing Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>

<img src="{GIFS['snake']}" width="700"/>
"""),
    wrap("githubStats", """
## 💥 Burn Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=FF6B35&icon_color=FF6B35&text_color=ff9a9a" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=FF6B35&text_color=ff9a9a" height="160"/>
</p>
"""),
    wrap("streak", """
## 🔥 Inferno Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=radical&hide_border=true&background=0D0D0D&ring=FF6B35&fire=FF0000&currStreakLabel=FF6B35" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Language Inferno

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=FF6B35&text_color=ff9a9a"/>
</p>
"""),
    wrap("projects", """
## 🚀 Rockets

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=FF6B35&text_color=ffffff"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=FF6B35&text_color=ffffff"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📡 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FF6B35?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FF6B35?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-FF6B35?style=for-the-badge&logo=firefox&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-FF6B35?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 🔥 Ignite

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Trophies Earned

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Hall of Flame

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5,2,1&height=120&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# RETRO / TERMINAL THEME
# ══════════════════════════════════════════════════════════════════════════

templates["24-retro-terminal.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0a0a0a&height=4" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=38&pause=400&color=33FF33&center=true&vCenter=true&width=700&lines=C%3A%5C%3E+BOOT+SEQUENCE+COMPLETE;C%3A%5C%3E+LOADING+YOUR_NAME...;C%3A%5C%3E+ROLE%3A+YOUR_ROLE;C%3A%5C%3E+STATUS%3A+ONLINE+✓;C%3A%5C%3E+READY_" alt="Retro Boot"/>
</div>
"""),
    wrap("about", """
## 💾 SYSTEM INFO

```
╔══════════════════════════════════════════════════════════╗
║             SYSTEM INFORMATION v2.0                      ║
╠══════════════════════════════════════════════════════════╣
║  USER     > YOUR_NAME                                    ║
║  ROLE     > YOUR_ROLE                                    ║
║  COMPANY  > YOUR_COMPANY                                 ║
║  LOCATION > YOUR_CITY, YOUR_COUNTRY                      ║
║  PROJECT  > YOUR_PROJECT                                 ║
║  LEARNING > YOUR_LEARNING                                ║
║  EMAIL    > YOUR_EMAIL                                   ║
║  FUN FACT > YOUR_FUN_FACT                                ║
╚══════════════════════════════════════════════════════════╝
```
"""),
    wrap("techStack", """
## 🖥️ TECH_STACK.EXE

```
> RUNNING STACK SCAN...

  ✔ LANGUAGES   : YOUR_TOPICS
  ✔ TOOLS       : YOUR_TOOLS

> SCAN COMPLETE [100%] ██████████████████████████
```

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 GITHUB_STATS.EXE

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=chartreuse-dark&hide_border=true&bg_color=0a0a0a&title_color=33ff33&icon_color=33ff33&text_color=33ff33" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=chartreuse-dark&hide_border=true&bg_color=0a0a0a&title_color=33ff33&text_color=33ff33" height="160"/>
</p>
"""),
    wrap("streak", """
## 🔋 UPTIME.LOG

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0a0a0a&ring=33ff33&fire=33ff33&currStreakLabel=33ff33" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💿 LANGUAGES.DAT

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=chartreuse-dark&hide_border=true&bg_color=0a0a0a&title_color=33ff33&text_color=33ff33"/>
</p>
"""),
    wrap("projects", """
## 📁 PROJECTS DIR

```
> ls ~/projects/

  YOUR_PROJECT_1/    [ACTIVE]   → YOUR_PROJECT_1_DEMO
  YOUR_PROJECT_2/    [ACTIVE]   → YOUR_PROJECT_2_DEMO

> _
```
"""),
    wrap("socials", """
## 📡 CONNECT.EXE

```
> TRANSMISSION CHANNELS:
  [T] TWITTER  :: https://twitter.com/YOUR_TWITTER
  [L] LINKEDIN :: https://linkedin.com/in/YOUR_LINKEDIN
  [W] WEBSITE  :: YOUR_WEBSITE
  [E] EMAIL    :: YOUR_EMAIL
> _
```
"""),
    wrap("quote", """
## 💬 QUOTE.TXT

```
> cat quote.txt
"YOUR_QUOTE"
> _
```
"""),
    wrap("badges", """
## 🏅 ACHIEVEMENTS.DAT

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=matrix&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 TROPHIES.DAT

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=matrix&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0a0a0a&height=4" width="100%"/>
<br/>
<sub>[ SYSTEM ONLINE | YOUR_NAME.exe | 99.9% UPTIME ]</sub>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# AURORA / NORDIC THEME
# ══════════════════════════════════════════════════════════════════════════

templates["25-aurora-nordic.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:2E3440,50:88C0D0,100:EBCB8B&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=ECEFF4&animation=fadeIn&fontAlignY=38&desc=YOUR_ROLE&descAlignY=62&descFontColor=D8DEE9" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1500&color=88C0D0&center=true&vCenter=true&width=700&lines=Northern+Lights+Developer+🌌;YOUR_ROLE;YOUR_TAGLINE;Building+YOUR_PROJECT" alt="Aurora Typing"/>
</div>
"""),
    wrap("about", """
## ❄️ About Me

<table>
<tr><td>❄️ <b>Name</b></td><td>YOUR_NAME</td></tr>
<tr><td>🧊 <b>Role</b></td><td>YOUR_ROLE</td></tr>
<tr><td>🌨️ <b>Company</b></td><td>YOUR_COMPANY</td></tr>
<tr><td>🏔️ <b>Location</b></td><td>YOUR_CITY, YOUR_COUNTRY</td></tr>
<tr><td>🌿 <b>Building</b></td><td>YOUR_PROJECT</td></tr>
<tr><td>📚 <b>Learning</b></td><td>YOUR_LEARNING</td></tr>
<tr><td>📧 <b>Email</b></td><td>YOUR_EMAIL</td></tr>
</table>
"""),
    wrap("techStack", """
## 🧊 Frost Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Nordic Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=nord&hide_border=true" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=nord&hide_border=true" height="160"/>
</p>
"""),
    wrap("streak", """
## ❄️ Ice Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=nord&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 🌌 Language Aurora

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=nord&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## 🏔️ Expeditions

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=nord&hide_border=true"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=nord&hide_border=true"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🌐 Connections

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-88C0D0?style=for-the-badge&logo=twitter&logoColor=2E3440"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-5E81AC?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-EBCB8B?style=for-the-badge&logo=google-chrome&logoColor=2E3440"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-BF616A?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 🌌 Aurora Quote

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
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:2E3440,50:88C0D0,100:EBCB8B&height=120&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# MATRIX / CODE RAIN THEME
# ══════════════════════════════════════════════════════════════════════════

templates["26-matrix-rain.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="{GIFS['matrix']}" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Source+Code+Pro&size=16&duration=1500&pause=100&color=00FF41&center=true&vCenter=true&multiline=true&width=600&height=120&lines=01001000+01100101+01101100+01101100+01101111;Wake+up%2C+Neo...;IDENTITY%3A+YOUR_NAME;ROLE%3A+YOUR_ROLE;Follow+the+white+rabbit+🐇" alt="Matrix Typing"/>
</div>
"""),
    wrap("about", """
## 🐇 Profile

```diff
+ IDENTITY CONFIRMED
+ NAME: YOUR_NAME
+ SPECIALIZATION: YOUR_ROLE
+ COMPANY: YOUR_COMPANY
+ STATUS: PLUGGED IN
+ LOCATION: YOUR_CITY
+ MISSION: YOUR_PROJECT
+ LEARNING: YOUR_LEARNING
+ EMAIL: YOUR_EMAIL
```

```
[SKILLS MATRIX LOADED]

>> YOUR_TOPICS
>> YOUR_TOOLS
```
"""),
    wrap("techStack", f"""
## 💊 Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>

<img src="{GIFS['hack']}" width="200"/>
"""),
    wrap("githubStats", """
## 📊 The Numbers

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=merko&hide_border=true&bg_color=0a0a0a&title_color=00FF41&icon_color=00FF41&text_color=00cc33" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=merko&hide_border=true&bg_color=0a0a0a&title_color=00FF41&text_color=00cc33" height="160"/>
</p>
"""),
    wrap("streak", """
## 🟢 System Uptime

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=merko&hide_border=true&background=0a0a0a&ring=00FF41&fire=00FF41&currStreakLabel=00FF41" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💾 Language Registry

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=merko&hide_border=true&bg_color=0a0a0a&title_color=00FF41&text_color=00cc33"/>
</p>
"""),
    wrap("projects", """
## 📂 Programs

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=merko&hide_border=true&bg_color=0a0a0a&title_color=00FF41&text_color=00cc33"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=merko&hide_border=true&bg_color=0a0a0a&title_color=00FF41&text_color=00cc33"/>
  </a>
</p>
"""),
    wrap("socials", """
## 📡 Frequency

```
TRANSMISSION CHANNELS:
[T] TWITTER  :: https://twitter.com/YOUR_TWITTER
[L] LINKEDIN :: https://linkedin.com/in/YOUR_LINKEDIN
[W] WEB      :: YOUR_WEBSITE
[E] EMAIL    :: YOUR_EMAIL
```
"""),
    wrap("quote", """
## 💬 BROADCAST.TXT

> YOUR_QUOTE
"""),
    wrap("badges", """
## 🏅 Access Level

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=matrix&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## 🏆 Achievement Unlocked

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=matrix&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<sub>[ SYSTEM ONLINE | FOLLOW THE WHITE RABBIT ]</sub>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# GRADIENT CARD THEME (Modern SaaS-Style)
# ══════════════════════════════════════════════════════════════════════════

templates["27-gradient-cards.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,14,24&height=220&section=header&text=YOUR_NAME&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=YOUR_ROLE+%7C+YOUR_TAGLINE&descAlignY=62&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=22&pause=1500&color=6EE7B7&center=true&vCenter=true&width=700&lines=Building+the+future+🚀;YOUR_ROLE;YOUR_TAGLINE" alt="Gradient Typing"/>

<img src="{GIFS['laptop']}" width="400"/>
</div>
"""),
    wrap("about", """
## 👋 Hello World

<table>
<tr>
<td width="50%">

### Quick Facts
🔭 Building **YOUR_PROJECT**  
🌱 Learning **YOUR_LEARNING**  
💼 **YOUR_ROLE** @ **YOUR_COMPANY**  
📍 **YOUR_CITY, YOUR_COUNTRY**  
📫 **YOUR_EMAIL**  
⚡ **YOUR_FUN_FACT**  

</td>
<td width="50%">

<img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=6EE7B7&icon_color=6EE7B7&text_color=94A3B8" height="180"/>

</td>
</tr>
</table>
"""),
    wrap("techStack", """
## 🛠️ Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=github_dark&hide_border=true&count_private=true" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=github_dark&hide_border=true" height="160"/>
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
## 🚀 Projects

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
## 🌐 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-6EE7B7?style=for-the-badge&logo=twitter&logoColor=black"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-6EE7B7?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-6EE7B7?style=for-the-badge&logo=vercel&logoColor=black"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-6EE7B7?style=for-the-badge&logo=gmail&logoColor=black"/></a>
</p>
"""),
    wrap("quote", """
## 💬 Quote

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
    wrap("gifs", f"""
<div align="center">
  <img src="{GIFS['div_bar']}" width="700"/>
</div>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,14,24&height=120&section=footer" width="100%"/>
<img src="https://komarev.com/ghpvc/?username=YOUR_USERNAME&style=for-the-badge&color=6EE7B7" alt="Profile Views"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# MONOCHROME / CLEAN MINIMAL THEME
# ══════════════════════════════════════════════════════════════════════════

templates["28-mono-clean.md"] = "\n\n".join([
    wrap("header", """
<div align="center">
<br/>

# YOUR_NAME

**YOUR_ROLE · YOUR_CITY, YOUR_COUNTRY**

<img src="https://readme-typing-svg.demolab.com?font=IBM+Plex+Mono&weight=400&size=16&pause=3000&color=888888&center=true&vCenter=true&width=600&lines=YOUR_TAGLINE;Building+YOUR_PROJECT;Learning+YOUR_LEARNING" alt="Mono Typing"/>

<br/>

[![Twitter](https://img.shields.io/badge/Twitter-gray?style=flat&logo=twitter)](https://twitter.com/YOUR_TWITTER)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-gray?style=flat&logo=linkedin)](https://linkedin.com/in/YOUR_LINKEDIN)
[![Website](https://img.shields.io/badge/Website-gray?style=flat&logo=google-chrome)](YOUR_WEBSITE)
[![Email](https://img.shields.io/badge/Email-gray?style=flat&logo=gmail)](mailto:YOUR_EMAIL)

---
</div>
"""),
    wrap("about", """
## About

| | |
|:--|:--|
| 🏢 Company | YOUR_COMPANY |
| 💼 Role | YOUR_ROLE |
| 📍 Location | YOUR_CITY, YOUR_COUNTRY |
| 🔭 Building | YOUR_PROJECT |
| 🌱 Learning | YOUR_LEARNING |
| 🎯 Goal | YOUR_GOAL |
| 📧 Email | YOUR_EMAIL |
"""),
    wrap("techStack", """
## Stack

<p>
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=10&theme=light"/>
</p>
<p>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=10&theme=light"/>
</p>
"""),
    wrap("githubStats", """
## Stats

<p>
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=default&hide_border=true&title_color=000&icon_color=000&text_color=555" height="155"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=default&hide_border=true" height="155"/>
</p>
"""),
    wrap("streak", """
## Streak

<p>
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=default&hide_border=true" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## Top Languages

<p>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=default&hide_border=true"/>
</p>
"""),
    wrap("projects", """
## Projects

- **[YOUR_PROJECT_1](YOUR_PROJECT_1_DEMO)** — YOUR_PROJECT_1_DESC
- **[YOUR_PROJECT_2](YOUR_PROJECT_2_DEMO)** — YOUR_PROJECT_2_DESC
"""),
    wrap("socials", """
## Connect

[Twitter](https://twitter.com/YOUR_TWITTER) · [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN) · [Website](YOUR_WEBSITE) · [Email](mailto:YOUR_EMAIL)
"""),
    wrap("quote", """
## Quote

> YOUR_QUOTE
"""),
    wrap("badges", """
## Badges

<p>
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=flat&no-frame=true&row=1&column=6"/>
</p>
"""),
    wrap("trophies", """
## Trophies

<p>
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=flat&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<sub>⭐ Thanks for visiting · YOUR_NAME</sub>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# PURPLE GALAXY THEME
# ══════════════════════════════════════════════════════════════════════════

templates["29-purple-galaxy.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=17,20,24&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=38&desc=YOUR_ROLE&descAlignY=62" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=C084FC&center=true&vCenter=true&width=700&lines=YOUR_TAGLINE;YOUR_ROLE+✨;Building+YOUR_PROJECT" alt="Purple Typing"/>

<img src="{GIFS['rocket']}" width="150"/>
</div>
"""),
    wrap("about", """
## 🔮 About

- 🚀 Working on **YOUR_PROJECT**
- 🏢 At **YOUR_COMPANY**
- 💼 Role: **YOUR_ROLE**
- 📍 **YOUR_CITY, YOUR_COUNTRY**
- 🌱 Learning **YOUR_LEARNING**
- 🎯 **YOUR_GOAL**
- 📧 **YOUR_EMAIL**
- ⚡ **YOUR_FUN_FACT**
"""),
    wrap("techStack", """
## ✨ Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=midnight-purple&hide_border=true" height="160"/>
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
## 🌌 Projects

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
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-C084FC?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-9333EA?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-C084FC?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-9333EA?style=for-the-badge&logo=gmail&logoColor=white"/></a>
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
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=17,20,24&height=120&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# TEAL / EMERALD THEME
# ══════════════════════════════════════════════════════════════════════════

templates["30-teal-emerald.md"] = "\n\n".join([
    wrap("header", f"""
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:0D9488,100:10B981&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=YOUR_ROLE&descAlignY=62" width="100%"/>

<img src="{GIFS['coding']}" width="300"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1200&color=10B981&center=true&vCenter=true&width=700&lines=YOUR_ROLE+🌿;YOUR_TAGLINE;Building+YOUR_PROJECT" alt="Teal Typing"/>
</div>
"""),
    wrap("about", """
## 🌿 About Me

```json
{
  "name":     "YOUR_NAME",
  "role":     "YOUR_ROLE",
  "company":  "YOUR_COMPANY",
  "location": "YOUR_CITY, YOUR_COUNTRY",
  "building": "YOUR_PROJECT",
  "learning": "YOUR_LEARNING",
  "goal":     "YOUR_GOAL",
  "email":    "YOUR_EMAIL"
}
```
"""),
    wrap("techStack", """
## 🔧 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=YOUR_TOPICS&perline=8"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=YOUR_TOOLS&perline=8"/>
</p>
"""),
    wrap("githubStats", """
## 📊 Stats

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=vue-dark&hide_border=true&title_color=10B981&icon_color=10B981" height="160"/>
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=vue-dark&hide_border=true&title_color=10B981" height="160"/>
</p>
"""),
    wrap("streak", """
## 🔥 Streak

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YOUR_USERNAME&theme=vue-dark&hide_border=true&ring=10B981&fire=10B981&currStreakLabel=10B981" width="55%"/>
</p>
"""),
    wrap("topLangs", """
## 💡 Top Languages

<p align="center">
  <img src="https://github-readmeapp.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=vue-dark&hide_border=true&title_color=10B981"/>
</p>
"""),
    wrap("projects", """
## 🌱 Projects

<p align="center">
  <a href="YOUR_PROJECT_1_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=vue-dark&hide_border=true&title_color=10B981"/>
  </a>
  <a href="YOUR_PROJECT_2_DEMO">
    <img src="https://github-readmeapp.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=vue-dark&hide_border=true&title_color=10B981"/>
  </a>
</p>
"""),
    wrap("socials", """
## 🌐 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-10B981?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0D9488?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-10B981?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-0D9488?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
"""),
    wrap("quote", """
## 🌿 Quote

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
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=vue&no-frame=true&row=2&column=4"/>
</p>
"""),
    wrap("footer", """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0:0D9488,100:10B981&height=120&section=footer" width="100%"/>
</div>
"""),
])


# ══════════════════════════════════════════════════════════════════════════
# Write all files
# ══════════════════════════════════════════════════════════════════════════

# Delete old templates (01-16) to replace with fresh ones from v2 script
# This script only writes 17-30 (new ones)
count = 0
for filename, content in templates.items():
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    count += 1

print(f"✅ Generated {count} new templates in ./{OUT}/")
print()
for name in sorted(templates.keys()):
    print(f"  • {name}")

print()
print("📌 Notes:")
print("  • All placeholders use YOUR_* standard format")
print("  • All stat URLs use: github-readmeapp.vercel.app")
print("  • All streak URLs use: streak-stats.demolab.com")
print("  • All trophy URLs use: github-profile-trophy.vercel.app")
print("  • All skill URLs use: skillicons.dev")
print("  • All GIF URLs from: github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub")
print("  • Section markers: <!-- SECTION:id --> ... <!-- /SECTION:id -->")
