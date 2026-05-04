import os

OUT = "/md-templates"
os.makedirs(OUT, exist_ok=True)

templates = {}

# ─────────────────────────────────────────────────────────────
# MINIMAL TEMPLATES (1-6)
# ─────────────────────────────────────────────────────────────

templates["01-minimal-classic.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=YOUR_NAME&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=YOUR_TAGLINE&descAlignY=55&descAlign=50" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=435&lines=Hi+there%2C+I'm+YOUR_NAME+%F0%9F%91%8B;Welcome+to+my+GitHub+Profile!;I+build+things+for+the+web" alt="Typing SVG" />

---

### 👨‍💻 About Me

```yaml
name: YOUR_NAME
location: YOUR_CITY, YOUR_COUNTRY
role: YOUR_ROLE
focus: YOUR_FOCUS
learning: YOUR_CURRENTLY_LEARNING
```

---

### 🛠 Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,nodejs,python,git,docker&perline=8" />
</p>

---

### 📊 GitHub Stats

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=58A6FF&text_color=c9d1d9&icon_color=58A6FF" />
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=transparent&hide_border=true&title_color=58A6FF&text_color=c9d1d9" />
</p>

---

### 🤝 Connect With Me

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>
"""

templates["02-minimal-dark.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0d1117&height=2&section=header" width="100%"/>

<br/>

```
██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ███╗   ██╗ █████╗ ███╗   ███╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ████╗  ██║██╔══██╗████╗ ████║██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ██╔██╗ ██║███████║██╔████╔██║█████╗  
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
```

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=2000&pause=800&color=00FF41&center=true&vCenter=true&width=600&lines=~/dev+%24+whoami;%3E+YOUR_NAME+%7C+YOUR_ROLE;%3E+Building+in+the+dark...;%3E+Coffee+%2B+Code+%3D+%E2%9D%A4%EF%B8%8F" alt="Typing SVG"/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700"/>

---

<table>
<tr>
<td valign="top" width="50%">

**`// about_me.js`**
```javascript
const me = {
  name: "YOUR_NAME",
  role: "YOUR_ROLE",
  location: "YOUR_LOCATION",
  workingOn: "YOUR_PROJECT",
  learning: ["YOUR_SKILL_1", "YOUR_SKILL_2"],
  askMeAbout: ["web", "tech", "dev"],
  funFact: "YOUR_FUN_FACT"
};
```

</td>
<td valign="top" width="50%">

**`// stack.sh`**
```bash
$ ls ~/tech-stack
frontend/   → React • Next.js • TypeScript
backend/    → Node • Python • Go
database/   → PostgreSQL • MongoDB
devops/     → Docker • K8s • AWS
tools/      → Git • Linux • VS Code
```

</td>
</tr>
</table>

---

<img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0D1117&ring=00FF41&fire=00FF41&currStreakLabel=00FF41" width="60%"/>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/-Twitter-black?style=flat-square&logo=twitter"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/-LinkedIn-black?style=flat-square&logo=linkedin"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/-Email-black?style=flat-square&logo=gmail"/></a>

</div>
"""

templates["03-minimal-pastel.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=0,2,2,5,30&height=200&section=header&text=Hello%2C+I'm+YOUR_NAME+%F0%9F%8C%B8&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=YOUR_TAGLINE&descAlignY=62" width="100%"/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="400"/>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Nunito&size=20&pause=1000&color=FF6B9D&center=true&vCenter=true&width=500&lines=Passionate+about+clean+code+%F0%9F%8C%9F;Turning+coffee+into+commits+%E2%98%95;Building+beautiful+interfaces+%F0%9F%8E%A8;Always+learning+something+new+%F0%9F%93%9A" alt="Typing SVG"/>

---

<table border="0" align="center">
<tr>
<td>

🌍 **Location:** YOUR_CITY, YOUR_COUNTRY  
💼 **Role:** YOUR_ROLE  
🔭 **Working on:** YOUR_PROJECT  
🌱 **Learning:** YOUR_LEARNING  
💬 **Ask me about:** YOUR_TOPICS  
⚡ **Fun fact:** YOUR_FUN_FACT  

</td>
<td>

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=graywhite&hide_border=true&title_color=FF6B9D&icon_color=FF6B9D" />

</td>
</tr>
</table>

---

### 🎀 Skills

<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,ts,react,vue,figma,git&perline=8" />
</p>

---

### 🌸 Connect

[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/YOUR_TWITTER)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN)
[![Portfolio](https://img.shields.io/badge/Portfolio-%23FF6B9D.svg?style=for-the-badge&logo=netlify&logoColor=white)](https://YOUR_WEBSITE)

</div>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer" width="100%"/>
"""

templates["04-minimal-neon.md"] = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=9,17,24&height=300&section=header&text=YOUR_NAME&fontSize=80&fontColor=00FFFF&animation=twinkling&fontAlignY=40&desc=YOUR_ROLE&descSize=24&descFontColor=FF00FF&descAlignY=62" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=20&pause=1000&color=00FFFF&center=true&vCenter=true&width=600&lines=SYSTEM+ONLINE+%F0%9F%9F%A2;LOADING+DEVELOPER+PROFILE...;HACK+THE+PLANET+%F0%9F%8C%90;YOUR_TAGLINE" alt="Typing SVG"/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400"/>

---

<table>
<tr>
<td>

```
╔══════════════════════════════╗
║  DEVELOPER_PROFILE_v2.0      ║
╠══════════════════════════════╣
║  NAME    : YOUR_NAME         ║
║  ROLE    : YOUR_ROLE         ║
║  STATUS  : [BUILDING]        ║
║  UPTIME  : 99.9%             ║
║  FOCUS   : YOUR_FOCUS        ║
╚══════════════════════════════╝
```

</td>
<td>

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical&hide_border=true&title_color=00FFFF&text_color=FF00FF&icon_color=00FFFF&bg_color=0d0d0d" />

</td>
</tr>
</table>

---

### ⚡ Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nodejs,python,rust,docker,kubernetes,aws&perline=8&theme=dark" />
</p>

---

### 📡 Signal

[![Twitter](https://img.shields.io/badge/Twitter-00FFFF?style=for-the-badge&logo=twitter&logoColor=black)](https://twitter.com/YOUR_TWITTER)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-FF00FF?style=for-the-badge&logo=linkedin&logoColor=black)](https://linkedin.com/in/YOUR_LINKEDIN)

<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=9,17,24&height=150&section=footer" width="100%"/>

</div>
"""

templates["05-minimal-mono.md"] = """<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=000000&height=160&section=header&text=YOUR_NAME&fontSize=42&fontColor=ffffff&fontAlignY=35&desc=YOUR_ROLE&descAlignY=55">
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=ffffff&height=160&section=header&text=YOUR_NAME&fontSize=42&fontColor=000000&fontAlignY=35&desc=YOUR_ROLE&descAlignY=55">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=000000&height=160&section=header&text=YOUR_NAME&fontSize=42&fontColor=ffffff&fontAlignY=35" width="100%"/>
</picture>

<img src="https://readme-typing-svg.demolab.com?font=IBM+Plex+Mono&size=16&pause=1500&color=888888&center=true&vCenter=true&width=600&lines=print(%22Hello%2C+World!%22);%3E+YOUR_NAME;%3E+YOUR_ROLE;%3E+YOUR_TAGLINE" alt="Typing SVG"/>

---

&nbsp; **About**

| Key | Value |
|-----|-------|
| 🏠 Location | YOUR_CITY |
| 💼 Role | YOUR_ROLE |
| 🔭 Building | YOUR_PROJECT |
| 📚 Learning | YOUR_LEARNING |
| 📧 Email | YOUR_EMAIL |

---

&nbsp; **Stack**

`TypeScript` `JavaScript` `Python` `React` `Node.js` `PostgreSQL` `Docker` `Git`

---

&nbsp; **Stats**

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=default&hide_border=false&title_color=000&icon_color=000&text_color=555&bg_color=ffffff" height="150"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=default&hide_border=false&title_color=000&text_color=555" height="150"/>

---

[Twitter](https://twitter.com/YOUR_TWITTER) · [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN) · [Website](https://YOUR_WEBSITE) · [Email](mailto:YOUR_EMAIL)

</div>
"""

templates["06-minimal-retro.md"] = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=0,0,0,12,12&height=200&section=header&text=YOUR_NAME&fontSize=60&fontColor=33ff33&animation=blinking&fontAlignY=45" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=28&pause=500&color=33FF33&center=true&vCenter=true&width=600&lines=C%3A%5C%3E+BOOT+SEQUENCE+COMPLETE;C%3A%5C%3E+LOADING+PROFILE...;C%3A%5C%3E+WELCOME+YOUR_NAME;C%3A%5C%3E+YOUR_ROLE;C%3A%5C%3E+READY_" alt="Typing SVG"/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100"/>

---

```
╔══════════════════════════════════════════════════════════╗
║             SYSTEM INFORMATION                           ║
╠══════════════════════════════════════════════════════════╣
║  USER     > YOUR_NAME                                    ║
║  VERSION  > 1.0.0                                        ║
║  BUILD    > YOUR_ROLE                                    ║
║  LOCATION > YOUR_CITY                                    ║
║  PROJECT  > YOUR_PROJECT                                 ║
║  OS       > macOS / Linux / Windows                      ║
╚══════════════════════════════════════════════════════════╝

> TECH_STACK.exe running...
  [████████████████████] 100%

  ✔ LANGUAGES   : YOUR_LANGUAGES
  ✔ FRAMEWORKS  : YOUR_FRAMEWORKS
  ✔ DATABASES   : YOUR_DATABASES
  ✔ TOOLS       : YOUR_TOOLS

> GITHUB_STATS.exe running...
```

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=chartreuse-dark&hide_border=true&bg_color=0d0d0d&title_color=33ff33&icon_color=33ff33&text_color=33ff33" />

```
> CONNECT.exe

  [T] TWITTER  : @YOUR_TWITTER
  [L] LINKEDIN : YOUR_LINKEDIN
  [W] WEBSITE  : YOUR_WEBSITE
  [E] EMAIL    : YOUR_EMAIL

> _
```

</div>
"""

# ─────────────────────────────────────────────────────────────
# ANIMATED TEMPLATES (7-12)
# ─────────────────────────────────────────────────────────────

templates["07-animated-typing.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&animation=fadeIn&fontAlignY=38&fontAlign=50" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=F75C7E&center=true&vCenter=true&multiline=true&random=false&width=600&height=100&lines=Hi+there!+I'm+YOUR_NAME+%F0%9F%91%8B;I'm+a+YOUR_ROLE;I+%E2%9D%A4%EF%B8%8F+Building+Amazing+Things" alt="Typing SVG"/>
</a>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/235224431-e8c8c12e-6826-47f1-89fb-2ddad83b3abf.gif" width="300"/>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=4000&pause=500&color=58A6FF&center=true&vCenter=true&multiline=false&width=700&lines=🔭+Currently+working+on+YOUR_PROJECT;🌱+Currently+learning+YOUR_LEARNING;💬+Ask+me+about+YOUR_TOPICS;📫+Reach+me+at+YOUR_EMAIL;⚡+Fun+fact%3A+YOUR_FUN_FACT" alt="Info SVG"/>

---

### 🚀 Technologies & Tools

<div align="center">
  <img src="https://skillicons.dev/icons?i=js,ts,react,nextjs,nodejs,express,python,fastapi&perline=8" />
  <br/>
  <img src="https://skillicons.dev/icons?i=mongodb,postgresql,redis,docker,kubernetes,aws,git,linux&perline=8" />
</div>

---

### 📊 My GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" height="165"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=tokyonight&hide_border=true" height="165"/>
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=tokyonight&hide_border=true" width="60%"/>
</div>

---

### 🤝 Let's Connect!

<div align="center">
  <a href="https://twitter.com/YOUR_TWITTER">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/>
  </a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://YOUR_WEBSITE">
    <img src="https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox-browser&logoColor=white"/>
  </a>
  <a href="mailto:YOUR_EMAIL">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
</div>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&pause=2000&color=58A6FF&center=true&vCenter=true&width=500&lines=Thanks+for+visiting!+%F0%9F%98%84;Star+%E2%AD%90+my+repos+if+you+find+them+helpful!" alt="Footer SVG"/>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>
"""

templates["08-animated-wave.md"] = """<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=white&animation=fadeIn&fontAlignY=38&desc=YOUR_ROLE+%7C+YOUR_TAGLINE&descAlignY=60&descAlign=50)

<img src="https://readme-typing-svg.demolab.com?font=Raleway&weight=700&size=24&pause=1200&color=764BA2&center=true&vCenter=true&random=false&width=500&lines=Building+the+future+%F0%9F%9A%80;One+commit+at+a+time+%F0%9F%92%AA;YOUR_TAGLINE" alt="Typing SVG" />

<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="900"/>

---

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🌊 About Me

🔭 Working on **YOUR_PROJECT**  
🌱 Learning **YOUR_LEARNING**  
👯 Looking to collaborate on **YOUR_COLLAB**  
💬 Ask me about **YOUR_TOPICS**  
📫 Email: **YOUR_EMAIL**  
⚡ Fun fact: **YOUR_FUN_FACT**  

</td>
<td width="50%" align="center">

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true&bg_color=1a1b27" height="180"/>

</td>
</tr>
</table>

---

### 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=react,nextjs,ts,tailwind,nodejs,express,python,fastapi,postgres,mongodb,redis,docker,aws,git,figma,vscode&perline=8"/>
</p>

---

<div align="center">

### 📈 Contribution Graph

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=tokyo-night&hide_border=true&bg_color=1a1b27)](https://github.com/YOUR_USERNAME)

</div>

---

### 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=tokyonight&no-frame=true&no-bg=false&margin-w=4&row=1"/>
</p>

---

### 📬 Connect

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-667eea?style=flat-square&logo=twitter&logoColor=white" height="30"/></a>&nbsp;
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-764ba2?style=flat-square&logo=linkedin&logoColor=white" height="30"/></a>&nbsp;
  <a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-667eea?style=flat-square&logo=google-chrome&logoColor=white" height="30"/></a>
</p>

</div>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=120&section=footer)
"""

templates["09-animated-space.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=galaxy&color=gradient&height=280&section=header&text=YOUR_NAME&fontSize=65&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Exploring+the+universe+of+code+🚀&descAlignY=60&descSize=18" width="100%"/>

<img src="https://user-images.githubusercontent.com/74038190/216644497-1951db19-8f3d-4e44-ac08-8e9d7e0d94a7.gif" width="200"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=18&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=🌌+Exploring+the+cosmos+of+code;🚀+Building+systems+that+scale+to+infinity;⭐+YOUR_TAGLINE;🪐+YOUR_ROLE" alt="Space Typing"/>

---

<br/>

<table>
<tr>
<td valign="top">

### 🌟 Mission Control

```
ASTRONAUT: YOUR_NAME
MISSION:   YOUR_PROJECT
SECTOR:    YOUR_LOCATION
STATUS:    🟢 ONLINE
FUEL:      ☕ Coffee
SKILLS:    YOUR_SKILLS
```

</td>
<td valign="top">

### 🛸 Fleet

<img src="https://skillicons.dev/icons?i=ts,react,nodejs,python,rust,go,docker,kubernetes&perline=4" />

</td>
<td valign="top">

### 🌠 Signal

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true&bg_color=0d0d2b&title_color=A78BFA&icon_color=A78BFA&text_color=c9d1d9" height="180"/>

</td>
</tr>
</table>

---

<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="900"/>

---

### 🚀 Launch Stats

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=midnight-purple&hide_border=true&background=0d0d2b&ring=A78BFA&fire=A78BFA&currStreakLabel=A78BFA" width="55%"/>
</p>

### 🌌 Activity Map

[![Activity](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=dracula&bg_color=0d0d2b&color=A78BFA&line=7C3AED&point=A78BFA&hide_border=true)](https://github.com/YOUR_USERNAME)

---

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-A78BFA?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=galaxy&color=gradient&height=150&section=footer" width="100%"/>

</div>
"""

templates["10-animated-fire.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5,2,1&height=220&section=header&text=YOUR_NAME&fontSize=60&fontColor=fff&animation=twinkling&fontAlignY=38&desc=YOUR_ROLE&descAlignY=60" width="100%"/>

<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="100"/>

<img src="https://readme-typing-svg.demolab.com?font=Bebas+Neue&size=32&pause=800&color=FF6B35&center=true&vCenter=true&width=600&lines=ON+FIRE+WITH+CODE+🔥;YOUR_TAGLINE;BUILDING+THE+IMPOSSIBLE;YOUR_ROLE" alt="Fire Typing"/>

---

### 🔥 The Blazing Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,nodejs,python,go,rust&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=graphql,postgres,redis,mongodb,docker,kubernetes,aws,gcp&perline=8"/>
</p>

---

<table>
<tr>
<td>

### ⚡ Quick Info

- 🔥 Working on: **YOUR_PROJECT**
- 💥 Speciality: **YOUR_SPECIALTY**
- 🌍 Based in: **YOUR_LOCATION**
- 📚 Learning: **YOUR_LEARNING**
- 🤝 Open to: **Collaboration**
- 🎯 Goal: **YOUR_GOAL**

</td>
<td>

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical&hide_border=true&bg_color=0d0d0d&title_color=FF6B35&icon_color=FF6B35&text_color=ff9a9a" height="160"/>

</td>
</tr>
</table>

---

### 💥 Burn Rate

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=radical&hide_border=true&background=0D0D0D&ring=FF6B35&fire=FF0000&currStreakLabel=FF6B35" width="55%"/>
</p>

### 🏅 Achievements

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1&column=7"/>
</p>

---

<p align="center">
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FF6B35?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FF6B35?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-FF6B35?style=for-the-badge&logo=firefox&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5,2,1&height=120&section=footer" width="100%"/>

</div>
"""

templates["11-animated-matrix.md"] = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0a0a0a&height=3" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Source+Code+Pro&size=14&duration=1500&pause=100&color=00FF41&center=true&vCenter=true&multiline=true&random=false&width=600&height=120&lines=01001000+01100101+01101100+01101100+01101111;Initializing+profile+for+YOUR_NAME...;Wake+up%2C+Neo...;The+Matrix+has+you...;Follow+the+white+rabbit+%F0%9F%90%87" alt="Matrix Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/216649426-0c2ee152-84d8-4707-85c4-27a378d2f78a.gif" width="450"/>

---

```diff
+ IDENTITY CONFIRMED
+ NAME: YOUR_NAME
+ SPECIALIZATION: YOUR_ROLE
+ STATUS: PLUGGED IN
+ MISSION: YOUR_PROJECT
+ SKILLS: LOADING...
```

```
[SKILLS MATRIX LOADED]

>> FRONTEND   ████████████████░░░░  80%
>> BACKEND    █████████████████░░░  85%
>> DEVOPS     ██████████████░░░░░░  70%
>> ALGORITHMS ████████████████████  99%
>> COFFEE     ████████████████████ 100%
```

---

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=merko&hide_border=true&bg_color=0a0a0a&title_color=00FF41&icon_color=00FF41&text_color=00cc33"/>

<img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=merko&hide_border=true&background=0a0a0a&ring=00FF41&fire=00FF41&currStreakLabel=00FF41"/>

---

```
TRANSMISSION CHANNELS:
[T]WITTER  :: https://twitter.com/YOUR_TWITTER
[L]INKEDIN :: https://linkedin.com/in/YOUR_LINKEDIN
[W]EB      :: https://YOUR_WEBSITE
[M]AIL     :: YOUR_EMAIL
```

</div>
"""

templates["12-animated-gradient.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3a1c71,50:d76d77,100:ffaf7b&height=200&section=header&text=Hello!+I'm+YOUR_NAME&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=YOUR_TAGLINE&descAlignY=60&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Pacifico&size=26&pause=1000&color=d76d77&center=true&vCenter=true&width=600&lines=Creative+Developer+🎨;Full+Stack+Enthusiast+💻;YOUR_TAGLINE+✨;Building+with+passion+❤️" alt="Gradient Typing"/>

<br/>
<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100"/>
<br/>

---

<img src="https://user-images.githubusercontent.com/74038190/212750147-854a394f-fee9-4080-9770-78a4b7ece53f.gif" width="900"/>

---

### 🎨 About

<p align="left">

- 🔭 I'm currently working on **YOUR_PROJECT**
- 🌱 I'm learning **YOUR_LEARNING**
- 👯 Looking to collaborate on **YOUR_COLLAB**
- 💬 Ask me about **YOUR_TOPICS**
- 📫 How to reach me: **YOUR_EMAIL**
- ⚡ Fun fact: **YOUR_FUN_FACT**

</p>

### 🌈 Tech Stack

<p>
  <img src="https://skillicons.dev/icons?i=html,css,js,ts,react,nextjs,tailwind,nodejs&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=python,django,postgres,mongo,redis,docker,vercel,figma&perline=8"/>
</p>

---

### ✨ Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=sunset-gradient&hide_border=true&count_private=true" height="160"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=sunset-gradient&hide_border=true" height="160"/>
</p>

---

### 💌 Connect

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-d76d77?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-3a1c71?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-ffaf7b?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3a1c71,50:d76d77,100:ffaf7b&height=100&section=footer" width="100%"/>

</div>
"""

# ─────────────────────────────────────────────────────────────
# FULL STACK TEMPLATES (13-18)
# ─────────────────────────────────────────────────────────────

templates["13-fullstack-modern.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Full+Stack+Developer&descAlignY=60&descSize=22" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=22D3EE&center=true&vCenter=true&width=700&lines=Full+Stack+Developer+%F0%9F%9A%80;React+%2B+Node.js+%2B+Cloud+%E2%98%81%EF%B8%8F;Building+scalable+applications;YOUR_TAGLINE" alt="Typing SVG"/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/229223156-0cbdaba9-3128-4d8e-8719-b6b4cf741b67.gif" width="400"/>

</div>

---

## 🧑‍💻 About Me

<img align="right" src="https://user-images.githubusercontent.com/74038190/212748842-9fcbad5b-6173-4175-8a61-521f3dbb7514.gif" width="300"/>

- 🔭 Currently building **YOUR_PROJECT**
- 🌱 Mastering **YOUR_LEARNING**
- 💡 Passionate about **clean architecture & DX**
- 🌍 Based in **YOUR_LOCATION**
- 📫 Reach me at **YOUR_EMAIL**
- ⚡ **YOUR_FUN_FACT**

<br clear="right"/>

---

## ⚙️ Tech Stack

### Frontend
<p>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tailwind-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white"/>
</p>

### Backend
<p>
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white"/>
  <img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

### Database & Cloud
<p>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

---

## 📊 GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" height="165"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=tokyonight&hide_border=true" height="165"/>
</div>
<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=tokyonight&hide_border=true" width="60%"/>
</div>

---

## 🌐 Connect

<div align="center">
  <a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-22D3EE?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12&height=100&section=footer" width="100%"/>
"""

templates["14-fullstack-terminal.md"] = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=1e1e2e&height=4&section=header" width="100%"/>

</div>

```
┌─────────────────────────────────────────────────────────────────────┐
│  Terminal v2.0                                          _ □ ×        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  $ whoami                                                            │
│  > YOUR_NAME — Full Stack Developer                                  │
│                                                                      │
│  $ cat about.txt                                                     │
│  > Building web applications from pixel to packet.                   │
│  > YOUR_TAGLINE                                                      │
│  > Based in: YOUR_LOCATION                                           │
│                                                                      │
│  $ ls ./projects                                                     │
│  > YOUR_PROJECT_1/  YOUR_PROJECT_2/  YOUR_PROJECT_3/                 │
│                                                                      │
│  $ cat stack.json                                                    │
│  {                                                                   │
│    "frontend": ["React", "Next.js", "TypeScript", "Tailwind"],       │
│    "backend":  ["Node.js", "Python", "Go", "GraphQL"],               │
│    "database": ["PostgreSQL", "MongoDB", "Redis"],                   │
│    "devops":   ["Docker", "K8s", "AWS", "Terraform"]                 │
│  }                                                                   │
│                                                                      │
│  $ git log --oneline -5                                              │
│  a1b2c3d  feat: shipped YOUR_FEATURE                                 │
│  e4f5g6h  fix: resolved YOUR_FIX                                     │
│  i7j8k9l  docs: updated README                                       │
│  m1n2o3p  refactor: cleaned up YOUR_MODULE                           │
│  q4r5s6t  chore: bumped dependencies                                 │
│                                                                      │
│  $ echo $CONTACT                                                     │
│  > twitter: @YOUR_TWITTER                                            │
│  > linkedin: YOUR_LINKEDIN                                           │
│  > email: YOUR_EMAIL                                                 │
│  > web: YOUR_WEBSITE                                                 │
│                                                                      │
│  $ _                                                                 │
└─────────────────────────────────────────────────────────────────────┘
```

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dark&hide_border=false&bg_color=1e1e2e&title_color=cba6f7&icon_color=89b4fa&text_color=cdd6f4&border_color=45475a" height="155"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dark&hide_border=false&bg_color=1e1e2e&title_color=cba6f7&text_color=cdd6f4&border_color=45475a" height="155"/>

<br/>

<img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,python,go,postgres,docker&perline=8"/>

</div>
"""

templates["15-fullstack-dashboard.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,20,14,5&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Full+Stack+Engineer&descAlignY=58" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=20&pause=2000&color=38BDF8&center=true&vCenter=true&width=600&lines=Frontend+%2B+Backend+%2B+Cloud+%3D+%F0%9F%9A%80;Building+products+people+love;YOUR_TAGLINE" alt="Dashboard Header"/>

---

</div>

<table>
<thead>
<tr>
<th>👤 Profile</th>
<th>📈 Metrics</th>
</tr>
</thead>
<tbody>
<tr>
<td>

| Field | Value |
|-------|-------|
| **Name** | YOUR_NAME |
| **Title** | Full Stack Developer |
| **Location** | YOUR_LOCATION |
| **Experience** | YOUR_YEARS yrs |
| **Status** | 🟢 Available |
| **Email** | YOUR_EMAIL |

</td>
<td>

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=38BDF8&icon_color=38BDF8&text_color=94A3B8" height="175"/>

</td>
</tr>
</tbody>
</table>

---

<div align="center">

## 🏗️ Architecture Skills

<table>
<tr>
<th>Layer</th>
<th>Technologies</th>
</tr>
<tr>
<td>🖥️ Frontend</td>
<td><img src="https://skillicons.dev/icons?i=react,nextjs,ts,tailwind,redux&perline=10"/></td>
</tr>
<tr>
<td>⚙️ Backend</td>
<td><img src="https://skillicons.dev/icons?i=nodejs,express,python,fastapi,graphql&perline=10"/></td>
</tr>
<tr>
<td>🗄️ Database</td>
<td><img src="https://skillicons.dev/icons?i=postgres,mongodb,redis,mysql,prisma&perline=10"/></td>
</tr>
<tr>
<td>☁️ DevOps</td>
<td><img src="https://skillicons.dev/icons?i=docker,kubernetes,aws,gcp,terraform&perline=10"/></td>
</tr>
</table>

## 📊 Activity Dashboard

<img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0f172a&ring=38BDF8&fire=38BDF8&currStreakLabel=38BDF8" width="50%"/>

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=github-compact&hide_border=true&bg_color=0f172a&color=38BDF8&line=0EA5E9&point=38BDF8)](https://github.com/YOUR_USERNAME)

## 🔗 Links

<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-38BDF8?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-0EA5E9?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-7C3AED?style=for-the-badge&logo=vercel&logoColor=white"/></a>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,20,14,5&height=100&section=footer" width="100%"/>
"""

templates["16-fullstack-creative.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=egg&color=gradient&customColorList=2,9,17&height=280&section=header&text=YOUR_NAME&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=42&desc=%F0%9F%9A%80+Full+Stack+Developer&descAlignY=65" width="100%"/>

<img src="https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif" width="500"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Pacifico&size=22&pause=1200&color=F9A826&center=true&vCenter=true&width=600&lines=Crafting+digital+experiences+%F0%9F%8E%A8;From+idea+to+deployment+%F0%9F%9A%80;Code+is+my+canvas+%F0%9F%96%8C%EF%B8%8F;YOUR_TAGLINE" alt="Creative Typing"/>

---

<p>

```javascript
// whoami.js
export const developer = {
  name:        "YOUR_NAME",
  title:       "Full Stack Developer",
  passion:     "Building products from 0 → 1",
  location:    "YOUR_LOCATION",
  workingOn:   "YOUR_PROJECT",
  learning:    ["YOUR_SKILL_1", "YOUR_SKILL_2"],
  dreamStack:  "TypeScript everywhere 🌎",
  coffee:      "Yes, always ☕"
};
```

</p>

---

### 🎨 My Palette (Tech)

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,python,go,postgres,redis,docker,aws,figma,git&perline=6"/>
</p>

---

<table>
<tr>
<td>

### 📊 Stats

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dracula&hide_border=true" height="155"/>

</td>
<td>

### 🔥 Streak

<img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=dracula&hide_border=true" height="155"/>

</td>
</tr>
</table>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-F9A826?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-F9A826?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
<a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-F9A826?style=for-the-badge&logo=firefox&logoColor=black"/></a>

</div>

<img src="https://capsule-render.vercel.app/api?type=egg&color=gradient&customColorList=2,9,17&height=150&section=footer" width="100%"/>
"""

templates["17-fullstack-neon.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,19,17,9,5&height=200&section=header&text=YOUR_NAME&fontSize=55&fontColor=39FF14&animation=twinkling&fontAlignY=38&desc=Full+Stack+%7C+Open+Source+%7C+Builder&descAlignY=60&descFontColor=FF00FF" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=20&pause=1000&color=39FF14&center=true&vCenter=true&width=700&lines=FULL+STACK+DEVELOPER+ONLINE+%F0%9F%9F%A2;REACT+%7C+NODE+%7C+CLOUD+INITIALIZED;BUILDING+YOUR_PROJECT...;YOUR_TAGLINE" alt="Neon Typing"/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="350"/>

---

```
┌──── SYSTEM SPECS ────────────────────────────────────┐
│                                                       │
│  ⬡ FRONTEND    React • Next.js • TypeScript          │
│  ⬡ STYLING     Tailwind • Framer Motion • GSAP       │
│  ⬡ BACKEND     Node.js • Python • Go • GraphQL       │
│  ⬡ DATABASE    PostgreSQL • MongoDB • Redis           │
│  ⬡ DEVOPS      Docker • K8s • AWS • Terraform        │
│                                                       │
│  STATUS: [████████████████████] READY                │
└───────────────────────────────────────────────────────┘
```

---

<table>
<tr>
<td>
<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=chartreuse-dark&hide_border=true&bg_color=0a0a0a&title_color=39FF14&icon_color=39FF14&text_color=39dd10" height="160"/>
</td>
<td>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=chartreuse-dark&hide_border=true&bg_color=0a0a0a&title_color=39FF14&text_color=39dd10" height="160"/>
</td>
</tr>
</table>

<img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=merko&hide_border=true&background=0a0a0a&ring=39FF14&fire=39FF14&currStreakLabel=39FF14" width="55%"/>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-39FF14?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FF00FF?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
<a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-39FF14?style=for-the-badge&logo=firefox&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,19,17,9,5&height=120&section=footer" width="100%"/>

</div>
"""

templates["18-fullstack-minimal.md"] = """<div align="center">

<br/>

# YOUR_NAME

**Full Stack Developer · YOUR_LOCATION**

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=400&size=16&pause=3000&color=6B7280&center=true&vCenter=true&width=600&lines=Building+scalable+web+applications;Open+to+collaborations+%26+opportunities;YOUR_TAGLINE" alt="Subtle Typing"/>

<br/>

[![Twitter](https://img.shields.io/badge/Twitter-gray?style=flat&logo=twitter)](https://twitter.com/YOUR_TWITTER)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-gray?style=flat&logo=linkedin)](https://linkedin.com/in/YOUR_LINKEDIN)
[![Website](https://img.shields.io/badge/Website-gray?style=flat&logo=google-chrome)](https://YOUR_WEBSITE)
[![Email](https://img.shields.io/badge/Email-gray?style=flat&logo=gmail)](mailto:YOUR_EMAIL)

---

### Stack

<p>
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,python,postgres,docker,aws&perline=8&theme=light"/>
</p>

---

### Stats

<p>
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=default&hide_border=true&title_color=000&icon_color=000&text_color=555" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=default&hide_border=true" height="155"/>
</p>

---

> *"YOUR_QUOTE"*

<br/>

</div>
"""

# ─────────────────────────────────────────────────────────────
# STUDENT / BEGINNER TEMPLATES (19-24)
# ─────────────────────────────────────────────────────────────

templates["19-student-journey.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6,14&height=200&section=header&text=Hi!+I'm+YOUR_NAME+%F0%9F%91%8B&fontSize=42&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Student+%7C+Aspiring+Developer&descAlignY=60" width="100%"/>

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="300"/>

<img src="https://readme-typing-svg.demolab.com?font=Nunito&size=20&pause=1000&color=34D399&center=true&vCenter=true&width=600&lines=Computer+Science+Student+%F0%9F%8E%93;Learning+to+code+one+bug+at+a+time+%F0%9F%90%9B;Passionate+about+tech+%F0%9F%9A%80;From+YOUR_UNIVERSITY" alt="Student Typing"/>

---

### 📚 About Me

| | |
|:--|:--|
| 🎓 **School** | YOUR_UNIVERSITY |
| 📖 **Major** | YOUR_MAJOR |
| 📅 **Year** | YOUR_YEAR |
| 🔭 **Building** | YOUR_PROJECT |
| 🌱 **Currently learning** | YOUR_LEARNING |
| 🎯 **Goal** | YOUR_GOAL |
| ⚡ **Fun fact** | YOUR_FUN_FACT |

---

### 🌱 My Learning Journey

```
FOUNDATIONS          [██████████] ✅ HTML, CSS, JS
JAVASCRIPT           [████████░░] 🚀 ES6+, DOM, APIs
REACT                [██████░░░░] 📚 Components, Hooks
NODE.JS              [████░░░░░░] 🌱 Express, REST APIs
DATABASES            [███░░░░░░░] 🌱 SQL Basics
GIT                  [███████░░░] 📚 Branching, PRs
```

---

### 🛠 Current Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,react,nodejs,git,github,vscode&perline=8"/>
</p>

---

### 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=vue&hide_border=true&count_private=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=vue&hide_border=true" height="155"/>
</p>

---

### 🤝 Let's Connect!

<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6,14&height=100&section=footer" width="100%"/>

</div>
"""

templates["20-student-goals.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=0:a8edea,100:fed6e3&height=180&section=header&text=YOUR_NAME&fontSize=50&fontColor=444&animation=fadeIn&fontAlignY=38&desc=Student+Developer+%7C+YOUR_UNIVERSITY&descFontColor=666&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Baloo+2&size=22&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Still+learning%2C+always+growing+%F0%9F%8C%B1;Turning+assignments+into+projects+%F0%9F%92%BB;Finding+bugs+%26+fixing+them+too+%F0%9F%90%9B;YOUR_TAGLINE" alt="Goals Typing"/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212749695-a6817c5a-a794-462b-afca-1b5ce7dd5e63.gif" width="350"/>

---

## 🎯 2025 Goals

- [ ] 🌐 Deploy **3 full-stack** projects
- [ ] 🧠 Complete **YOUR_COURSE** on Coursera/Udemy
- [ ] 🤝 Land my **first internship** in tech
- [ ] 🌱 Learn **YOUR_LANGUAGE**
- [ ] ⭐ Get **100 GitHub stars** total
- [ ] 📝 Start a **tech blog**

---

## 🌱 Learning Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,js,react,nodejs,git,html,css,linux&perline=8"/>
</p>

**Studying Next:**
<img src="https://skillicons.dev/icons?i=ts,nextjs,postgres,docker&perline=4"/>

---

## 📈 My Progress

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=buefy&hide_border=true&count_private=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=buefy&hide_border=true" height="155"/>
</p>

---

<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-6366F1?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-6366F1?style=for-the-badge&logo=gmail&logoColor=white"/></a>

</div>
"""

templates["21-student-cute.md"] = """<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/241765440-80728820-e06b-4f96-9c9e-9df46f0cc0a5.gif" width="300"/>

# Hi there! I'm YOUR_NAME 🌸

<img src="https://readme-typing-svg.demolab.com?font=Caveat&size=26&pause=1000&color=FF6B9D&center=true&vCenter=true&width=500&lines=Student+%40+YOUR_UNIVERSITY+%F0%9F%8E%93;Coding+%26+creating+%F0%9F%92%BB;Still+learning%2C+always+growing+%F0%9F%8C%B1;YOUR_TAGLINE+✨" alt="Cute Typing"/>

---

### 🎀 Little About Me

```
 ♡ Name     : YOUR_NAME
 ♡ Age      : YOUR_AGE
 ♡ School   : YOUR_UNIVERSITY
 ♡ Major    : YOUR_MAJOR
 ♡ Hobbies  : Coding, YOUR_HOBBY_1, YOUR_HOBBY_2
 ♡ Love     : Coffee ☕ & Clean Code ✨
 ♡ Currently: Learning YOUR_LEARNING
```

---

### 🌷 Tech I Use

<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,python,react,git,figma,vscode&perline=8"/>
</p>

---

### 📊 Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=rose_pine&hide_border=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=rose_pine&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FF6B9D?style=flat-square&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FF6B9D?style=flat-square&logo=linkedin&logoColor=white"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-FF6B9D?style=flat-square&logo=gmail&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFB6C1,100:FFD700&height=100&section=footer" width="100%"/>

</div>
"""

templates["22-student-explorer.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7,14,20&height=200&section=header&text=Explorer+%F0%9F%94%AD&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=YOUR_NAME+%7C+YOUR_UNIVERSITY&descAlignY=60" width="100%"/>

<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=FBBF24&center=true&vCenter=true&width=600&lines=Exploring+Computer+Science+%F0%9F%94%AD;Every+line+of+code+is+an+adventure;Building+skills+day+by+day+%F0%9F%92%AA;YOUR_TAGLINE" alt="Explorer Typing"/>

---

### 🗺️ My Dev Map

```
 🏔️ CONQUERED          🏕️ CAMPING            🗺️ PLANNING
 ─────────────         ──────────────        ─────────────
 HTML/CSS              React                 TypeScript
 JavaScript            Node.js               AWS
 Python basics         Git/GitHub            Docker
 Git basics            SQL                   Kubernetes
```

---

### 🧭 Toolkit

<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,python,react,nodejs,git,vscode&perline=8"/>
</p>

---

### 📡 Signal Strength (Stats)

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=ambient_gradient&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=ambient_gradient&hide_border=true" height="155"/>
</p>

---

<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FBBF24?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-FBBF24?style=for-the-badge&logo=gmail&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7,14,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["23-student-progress.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,12,7,3&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=%F0%9F%8E%93+CS+Student+%40+YOUR_UNIVERSITY&descAlignY=60&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Source+Code+Pro&size=18&pause=1500&color=10B981&center=true&vCenter=true&width=600&lines=Learning+in+public+%F0%9F%93%96;Building+projects+%F0%9F%94%A8;Debugging+my+future+%F0%9F%90%9B;YOUR_TAGLINE" alt="Progress Typing"/>

---

### 📊 Skill Progress

| Skill | Progress | Level |
|-------|----------|-------|
| Python | `████████░░` 80% | Intermediate |
| JavaScript | `██████░░░░` 60% | Learning |
| React | `████░░░░░░` 40% | Beginner |
| SQL | `█████░░░░░` 50% | Learning |
| Git | `███████░░░` 70% | Intermediate |
| Linux | `████░░░░░░` 40% | Beginner |

---

### 🔬 What I'm Studying

- 📘 **Data Structures & Algorithms** — LeetCode grind 💪
- 🌐 **Web Dev** — Building YOUR_PROJECT
- 🤖 **YOUR_SUBJECT** — Fascinating!
- 📚 **Reading** — *YOUR_BOOK*

---

### 🛠 Tools

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,js,html,css,react,git,linux,vscode&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=algolia&hide_border=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=algolia&hide_border=true" height="155"/>
</p>

---

<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-10B981?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-10B981?style=for-the-badge&logo=gmail&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,12,7,3&height=100&section=footer" width="100%"/>

</div>
"""

templates["24-student-hacker.md"] = r"""<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=40&pause=500&color=00FF41&center=true&vCenter=true&width=700&lines=BOOT+SEQUENCE+INITIALIZED...;STUDENT+DEVELOPER+ONLINE;NAME%3A+YOUR_NAME;SCHOOL%3A+YOUR_UNIVERSITY;STATUS%3A+LEARNING_%F0%9F%9F%A2" alt="Hacker Boot"/>

<img src="https://user-images.githubusercontent.com/74038190/212284119-fbfd994d-8c2a-4a07-a75f-84e513833c1c.gif" width="400"/>

---

```python
class Student:
    def __init__(self):
        self.name      = "YOUR_NAME"
        self.school    = "YOUR_UNIVERSITY"
        self.major     = "YOUR_MAJOR"
        self.year      = YOUR_YEAR
        self.skills    = ["Python", "JS", "React", "Git"]
        self.learning  = ["YOUR_SKILL_1", "YOUR_SKILL_2"]
        self.projects  = ["YOUR_PROJECT_1", "YOUR_PROJECT_2"]
        self.fun_fact  = "YOUR_FUN_FACT"

    def greet(self):
        return f"Hi, I'm {self.name}! Let's build something cool 🚀"

me = Student()
print(me.greet())
```

---

### 🧰 Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,js,html,css,react,git,linux,bash&perline=8" />
</p>

---

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=00FF41&icon_color=00FF41&text_color=00cc33" height="160"/>

<img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0d0d0d&ring=00FF41&fire=00FF41&currStreakLabel=00FF41" height="160"/>

---

`@YOUR_TWITTER` · `YOUR_LINKEDIN` · `YOUR_EMAIL`

</div>
"""

# ─────────────────────────────────────────────────────────────
# OPEN SOURCE TEMPLATES (25-30)
# ─────────────────────────────────────────────────────────────

templates["25-opensource-contributor.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Open+Source+Contributor+%F0%9F%8C%9F&descAlignY=60&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=FB923C&center=true&vCenter=true&width=700&lines=Open+source+is+my+playground+%F0%9F%8C%9F;PRs+welcome%2C+issues+too+%F0%9F%A4%9D;Making+software+free+for+everyone;YOUR_TAGLINE" alt="OSS Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100"/>

---

### 🌟 OSS Highlights

| Project | Description | Stars | Role |
|---------|-------------|-------|------|
| [YOUR_OSS_PROJECT_1](https://github.com/YOUR_USERNAME/YOUR_PROJECT_1) | YOUR_DESC_1 | ⭐ 0 | Maintainer |
| [YOUR_OSS_PROJECT_2](https://github.com/YOUR_USERNAME/YOUR_PROJECT_2) | YOUR_DESC_2 | ⭐ 0 | Contributor |
| [YOUR_OSS_PROJECT_3](https://github.com/YOUR_USERNAME/YOUR_PROJECT_3) | YOUR_DESC_3 | ⭐ 0 | Contributor |

---

### 🏅 Badges

<p align="center">
  <img src="https://img.shields.io/badge/Hacktoberfest-Participant-FF6B35?style=for-the-badge&logo=hacktoberfest&logoColor=white"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Open+Source-Lover-yellow?style=for-the-badge"/>
</p>

---

### 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nodejs,python,go,git,github&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=github_dark&hide_border=true&count_private=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=github-dark-blue&hide_border=true" height="155"/>
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=gitdimmed&no-frame=true&row=1"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Blog-FF6B35?style=for-the-badge&logo=hashnode&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["26-opensource-maintainer.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:e96c4c,100:e96c4c&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=OSS+Maintainer+%7C+YOUR_ROLE&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=E96C4C&center=true&vCenter=true&width=700&lines=Maintaining+open+source+projects+%F0%9F%94%A7;Code+reviews+are+an+act+of+love+%E2%9D%A4%EF%B8%8F;Building+communities+%F0%9F%91%AB;YOUR_TAGLINE" alt="Maintainer Typing"/>

---

### 🔧 Projects I Maintain

<table>
<tr>
<td align="center">
<a href="https://github.com/YOUR_USERNAME/YOUR_PROJECT_1">
<img src="https://github-readme-stats.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=solarized-light&hide_border=true"/>
</a>
</td>
<td align="center">
<a href="https://github.com/YOUR_USERNAME/YOUR_PROJECT_2">
<img src="https://github-readme-stats.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=solarized-light&hide_border=true"/>
</a>
</td>
</tr>
</table>

---

### 📊 Contribution Calendar

[![Activity](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=github-compact&hide_border=true)](https://github.com/YOUR_USERNAME)

---

### 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nodejs,python,rust,git,docker&perline=8"/>
</p>

---

### 🏆 Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-E96C4C?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-E96C4C?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:e96c4c,100:e96c4c&height=100&section=footer" width="100%"/>

</div>
"""

templates["27-opensource-hacker.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,20,14,9,5&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Hackathon+Winner+%7C+OSS+Hacker&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=16&pause=1000&color=A855F7&center=true&vCenter=true&width=700&lines=Hack+the+planet+%F0%9F%8C%8D;Built+in+48+hours%2C+ships+in+24+%F0%9F%9A%80;Breaking+things+to+build+better+ones;YOUR_HACKATHON_WINS+hackathon+wins+%F0%9F%8F%86" alt="Hacker Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700"/>

---

### 🏆 Hackathon Record

| Event | Project | Award |
|-------|---------|-------|
| YOUR_HACKATHON_1 | YOUR_PROJECT_1 | 🥇 1st Place |
| YOUR_HACKATHON_2 | YOUR_PROJECT_2 | 🥈 2nd Place |
| YOUR_HACKATHON_3 | YOUR_PROJECT_3 | 🎖 Best Design |

---

### ⚡ Quick Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,python,openai,supabase,vercel&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=midnight-purple&hide_border=true" height="155"/>
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=algolia&no-frame=true&row=1"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-A855F7?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://devpost.com/YOUR_DEVPOST"><img src="https://img.shields.io/badge/Devpost-A855F7?style=for-the-badge&logo=devpost&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-A855F7?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,20,14,9,5&height=100&section=footer" width="100%"/>

</div>
"""

templates["28-opensource-badges.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=22C55E&center=true&vCenter=true&width=600&lines=Open+Source+Contributor+%F0%9F%8C%9F;PRs+merged%3A+YOUR_PRS_COUNT+and+counting;YOUR_TAGLINE" alt="Badges Typing"/>

---

### 🏅 Achievement Badges

<p align="center">
  <img src="https://img.shields.io/badge/Hacktoberfest%202024-Completed-orange?style=for-the-badge&logo=hacktoberfest"/>
  <img src="https://img.shields.io/badge/PRs%20Merged-YOUR_COUNT-brightgreen?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/Issues%20Resolved-YOUR_COUNT-blue?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/Stars%20Earned-YOUR_COUNT-yellow?style=for-the-badge&logo=github"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Forks-YOUR_COUNT-9cf?style=flat-square&logo=github"/>
  <img src="https://img.shields.io/badge/Followers-YOUR_COUNT-success?style=flat-square&logo=github"/>
  <img src="https://img.shields.io/badge/Repos-YOUR_COUNT-blueviolet?style=flat-square&logo=github"/>
</p>

---

### 🛠 Technologies

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nodejs,python,go,rust,docker&perline=8"/>
  <img src="https://skillicons.dev/icons?i=postgres,mongodb,redis,graphql,aws,gcp,git,linux&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=vue-dark&hide_border=true&count_private=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=vue-dark&hide_border=true" height="155"/>
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=matrix&no-frame=true&row=1&column=8"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-22C55E?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-22C55E?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6&height=100&section=footer" width="100%"/>

</div>
"""

templates["29-opensource-community.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,20,24&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Community+Builder+%7C+OSS+Advocate&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=F59E0B&center=true&vCenter=true&width=700&lines=Code+together%2C+grow+together+%F0%9F%91%AB;YOUR_COMMUNITY_NAME+organizer+%F0%9F%93%A3;Mentoring+new+developers+%F0%9F%8C%B1;YOUR_TAGLINE" alt="Community Typing"/>

---

### 🤝 Community Work

- 🗣️ **Speaker** at YOUR_CONF_1, YOUR_CONF_2
- 📝 **Blogger** — YOUR_BLOG_COUNT articles written
- 🏫 **Mentor** — Helping YOUR_MENTEE_COUNT developers grow
- 📣 **Organizer** — YOUR_COMMUNITY_NAME
- 🎙️ **Podcast** — YOUR_PODCAST (if applicable)

---

### 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nodejs,python,docker,git,github&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=solarized-light&hide_border=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=solarized-light&hide_border=true" height="155"/>
</p>

[![Activity](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=github-compact&hide_border=true)](https://github.com/YOUR_USERNAME)

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-F59E0B?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-F59E0B?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
<a href="https://YOUR_BLOG"><img src="https://img.shields.io/badge/Blog-F59E0B?style=for-the-badge&logo=hashnode&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,20,24&height=100&section=footer" width="100%"/>

</div>
"""

templates["30-opensource-stats.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Powered+by+Contribution+%F0%9F%94%A5&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=F97316&center=true&vCenter=true&width=600&lines=YOUR_TOTAL_COMMITS%2B+commits+and+counting+%F0%9F%94%A5;YOUR_TOTAL_PRS%2B+pull+requests+merged;Contributing+since+YOUR_YEAR;YOUR_TAGLINE" alt="Stats Typing"/>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=onedark&hide_border=true&count_private=true&include_all_commits=true" height="165"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=onedark&hide_border=true&langs_count=10" height="165"/>
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=onedark&hide_border=true" width="55%"/>
</p>

[![Activity](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=one-dark&hide_border=true&bg_color=282c34&color=e06c75&line=e5c07b&point=61afef)](https://github.com/YOUR_USERNAME)

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=onedark&no-frame=true&row=1&column=8"/>
</p>

---

### 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nodejs,python,go,rust,docker,kubernetes,aws,git,linux&perline=6"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-F97316?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-F97316?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=100&section=footer" width="100%"/>

</div>
"""

# ─────────────────────────────────────────────────────────────
# DATA / AI TEMPLATES (31-36)
# ─────────────────────────────────────────────────────────────

templates["31-data-ai-researcher.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,14,9&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=AI+Researcher+%7C+YOUR_INSTITUTION&descAlignY=60&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=18&pause=1000&color=818CF8&center=true&vCenter=true&width=700&lines=Pushing+the+frontiers+of+AI+%F0%9F%A7%A0;Research+%3E+Deploy+%3E+Repeat;YOUR_RESEARCH_AREA+enthusiast;YOUR_TAGLINE" alt="AI Researcher Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100"/>

---

### 🧪 Research Interests

- 🤖 **YOUR_INTEREST_1** — YOUR_DESC_1
- 🧬 **YOUR_INTEREST_2** — YOUR_DESC_2
- 📊 **YOUR_INTEREST_3** — YOUR_DESC_3
- 🌐 **YOUR_INTEREST_4** — YOUR_DESC_4

---

### 📄 Publications

| Title | Venue | Year |
|-------|-------|------|
| [YOUR_PAPER_1](https://YOUR_PAPER_1_URL) | YOUR_VENUE_1 | 202X |
| [YOUR_PAPER_2](https://YOUR_PAPER_2_URL) | YOUR_VENUE_2 | 202X |

---

### 🛠 Research Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,sklearn,jupyter,docker,git,latex&perline=8"/>
</p>

**Libraries:** `transformers` `numpy` `pandas` `matplotlib` `wandb` `ray`

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dracula&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dracula&hide_border=true" height="155"/>
</p>

---

<a href="https://scholar.google.com/citations?user=YOUR_SCHOLAR_ID"><img src="https://img.shields.io/badge/Google Scholar-818CF8?style=for-the-badge&logo=google-scholar&logoColor=white"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-818CF8?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-818CF8?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,14,9&height=100&section=footer" width="100%"/>

</div>
"""

templates["32-data-ai-ml-engineer.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,9&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=ML+Engineer+%7C+YOUR_COMPANY&descAlignY=60&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=8B5CF6&center=true&vCenter=true&width=700&lines=Training+models+%F0%9F%A4%96;Deploying+AI+at+scale+%F0%9F%9A%80;Data+pipeline+architect+%F0%9F%94%A7;YOUR_TAGLINE" alt="ML Engineer Typing"/>

---

### 🤖 ML Stack

<table>
<tr>
<th>Category</th>
<th>Tools</th>
</tr>
<tr>
<td>🧠 Frameworks</td>
<td><img src="https://skillicons.dev/icons?i=pytorch,tensorflow&perline=10"/> + `JAX` `Hugging Face`</td>
</tr>
<tr>
<td>☁️ MLOps</td>
<td>`MLflow` `Weights & Biases` `DVC` `Airflow`</td>
</tr>
<tr>
<td>🗄️ Data</td>
<td><img src="https://skillicons.dev/icons?i=postgres,mongodb,kafka&perline=10"/> + `Spark` `Flink`</td>
</tr>
<tr>
<td>🚀 Serving</td>
<td>`FastAPI` `Triton` `BentoML` `Seldon`</td>
</tr>
<tr>
<td>☁️ Cloud</td>
<td><img src="https://skillicons.dev/icons?i=aws,gcp,docker,kubernetes&perline=10"/></td>
</tr>
</table>

---

### 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=midnight-purple&hide_border=true" height="155"/>
</p>

---

> 💬 *"YOUR_QUOTE"*

---

<a href="https://huggingface.co/YOUR_HF_USERNAME"><img src="https://img.shields.io/badge/HuggingFace-8B5CF6?style=for-the-badge&logo=huggingface&logoColor=white"/></a>
<a href="https://kaggle.com/YOUR_KAGGLE"><img src="https://img.shields.io/badge/Kaggle-8B5CF6?style=for-the-badge&logo=kaggle&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-8B5CF6?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,17,9&height=100&section=footer" width="100%"/>

</div>
"""

templates["33-data-ai-analyst.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,20,24&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Data+Analyst+%7C+Insights+Engineer&descAlignY=60&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Source+Code+Pro&size=18&pause=1000&color=06B6D4&center=true&vCenter=true&width=700&lines=Turning+data+into+decisions+%F0%9F%93%8A;SQL+wizard+%F0%9F%94%AE;Dashboards+that+tell+stories+%F0%9F%93%96;YOUR_TAGLINE" alt="Analyst Typing"/>

---

### 📊 Data Toolkit

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,r,postgres,mysql,mongodb,docker,git,aws&perline=8"/>
</p>

**Libraries & Tools:**
`pandas` `numpy` `matplotlib` `seaborn` `plotly`  
`dbt` `Airflow` `Spark` `Tableau` `Power BI` `Looker`

---

<table>
<tr>
<td>

### 📈 About Me

- 🏢 Work at: **YOUR_COMPANY**
- 📍 Based in: **YOUR_LOCATION**
- 🔭 Building: **YOUR_PROJECT**
- 📚 Learning: **YOUR_LEARNING**
- 📊 Specialty: **YOUR_SPECIALTY**

</td>
<td>

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=ocean_dark&hide_border=true" height="160"/>

</td>
</tr>
</table>

---

### 🗃️ Featured Notebooks

| Notebook | Description | Dataset |
|----------|-------------|---------|
| [YOUR_NOTEBOOK_1](https://kaggle.com/YOUR_USERNAME/YOUR_NB_1) | YOUR_DESC_1 | YOUR_DATA_1 |
| [YOUR_NOTEBOOK_2](https://kaggle.com/YOUR_USERNAME/YOUR_NB_2) | YOUR_DESC_2 | YOUR_DATA_2 |

---

<a href="https://kaggle.com/YOUR_KAGGLE"><img src="https://img.shields.io/badge/Kaggle-06B6D4?style=for-the-badge&logo=kaggle&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-06B6D4?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-06B6D4?style=for-the-badge&logo=twitter&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,20,24&height=100&section=footer" width="100%"/>

</div>
"""

templates["34-data-ai-deep-learning.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,17,20,24&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Deep+Learning+Engineer&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=loss.backward()+-+always+backpropagating;Training+transformers+%F0%9F%A4%96;Gradient+descent+into+madness+%F0%9F%94%A5;YOUR_TAGLINE" alt="DL Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212748830-4c709398-a386-4761-84d7-9e10b98fbe6e.gif" width="500"/>

---

### 🧠 Neural Network Stack

```python
model = Sequential([
    Dense("PyTorch", activation="expert"),
    Dense("TensorFlow", activation="intermediate"),
    Dense("JAX", activation="learning"),
    LSTM("Transformers", units=512),
    Attention("HuggingFace", heads=8),
    Dropout("Wandb", rate=0.0),
    Output("CUDA", units=1),
])
model.compile(optimizer="Adam", loss="MSE")
```

---

### 🛠 Toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,cuda,docker,aws,git,linux&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dracula&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dracula&hide_border=true&langs_count=8" height="155"/>
</p>

---

<a href="https://huggingface.co/YOUR_HF_USERNAME"><img src="https://img.shields.io/badge/Hugging Face-A78BFA?style=for-the-badge&logo=huggingface&logoColor=white"/></a>
<a href="https://kaggle.com/YOUR_KAGGLE"><img src="https://img.shields.io/badge/Kaggle-A78BFA?style=for-the-badge&logo=kaggle&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-A78BFA?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,17,20,24&height=100&section=footer" width="100%"/>

</div>
"""

templates["35-data-ai-nlp.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=17,20,24&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=NLP+Engineer+%7C+LLM+Developer&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=EC4899&center=true&vCenter=true&width=700&lines=Making+machines+understand+language+%F0%9F%A4%96;Fine-tuning+LLMs+since+YOUR_YEAR;Prompt+engineering+is+an+art+%F0%9F%8E%A8;YOUR_TAGLINE" alt="NLP Typing"/>

---

### 🗣️ NLP Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,fastapi,docker,aws,git&perline=6"/>
</p>

**Specialized Tools:**
`transformers` `spaCy` `NLTK` `LangChain` `LlamaIndex`  
`OpenAI API` `Anthropic Claude` `Pinecone` `Weaviate` `Chroma`

---

### 🤖 Projects

| Project | Description | Tech |
|---------|-------------|------|
| [YOUR_NLP_PROJECT_1](https://github.com/YOUR_USERNAME/YOUR_PROJECT_1) | YOUR_DESC_1 | YOUR_TECH_1 |
| [YOUR_NLP_PROJECT_2](https://github.com/YOUR_USERNAME/YOUR_PROJECT_2) | YOUR_DESC_2 | YOUR_TECH_2 |

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=midnight-purple&hide_border=true" height="155"/>
</p>

---

<a href="https://huggingface.co/YOUR_HF_USERNAME"><img src="https://img.shields.io/badge/Hugging Face-EC4899?style=for-the-badge&logo=huggingface&logoColor=white"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-EC4899?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-EC4899?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=17,20,24&height=100&section=footer" width="100%"/>

</div>
"""

templates["36-data-ai-vision.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,9,17&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Computer+Vision+Engineer&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=10B981&center=true&vCenter=true&width=700&lines=Teaching+machines+to+see+%F0%9F%91%81%EF%B8%8F;Object+detection+%F0%9F%8E%AF+segmentation+%F0%9F%A7%A9;YOUR_TAGLINE;YOLO+%7C+SAM+%7C+CLIP+%7C+ViT" alt="Vision Typing"/>

---

### 👁️ Vision Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,opencv,docker,cuda,aws,git,linux&perline=8"/>
</p>

**CV Libraries:** `OpenCV` `Pillow` `Albumentations` `detectron2`  
**Models:** `YOLO` `SAM` `CLIP` `ViT` `Stable Diffusion`  
**Tools:** `Label Studio` `Roboflow` `Wandb` `ONNX` `TensorRT`

---

### 📊 Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=algolia&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=algolia&hide_border=true" height="155"/>
</p>

---

<a href="https://kaggle.com/YOUR_KAGGLE"><img src="https://img.shields.io/badge/Kaggle-10B981?style=for-the-badge&logo=kaggle&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-10B981?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,9,17&height=100&section=footer" width="100%"/>

</div>
"""

# ─────────────────────────────────────────────────────────────
# WEB3 / BLOCKCHAIN TEMPLATES (37-42)
# ─────────────────────────────────────────────────────────────

templates["37-web3-defi.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=38&desc=DeFi+Developer+%7C+Protocol+Engineer&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=18&pause=1000&color=F59E0B&center=true&vCenter=true&width=700&lines=Building+decentralized+finance+%F0%9F%8F%A6;Smart+contract+auditor+%F0%9F%94%91;DeFi+protocols+%7C+AMMs+%7C+Lending;YOUR_TAGLINE" alt="DeFi Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100"/>

---

### ⛓️ Blockchain Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=solidity,ethereum,ts,js,react,nodejs,python,git&perline=8"/>
</p>

**Web3 Tools:** `Hardhat` `Foundry` `Ethers.js` `Viem` `Wagmi`  
**DeFi:** `Uniswap` `Aave` `Compound` `Chainlink`  
**Testing:** `Forge` `Echidna` `Slither` `MythX`

---

### 🔗 Deployed Contracts

| Protocol | Network | Address |
|----------|---------|---------|
| YOUR_CONTRACT_1 | Ethereum | `0x...` |
| YOUR_CONTRACT_2 | Polygon | `0x...` |

---

### 📊 Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=F59E0B&icon_color=F59E0B&text_color=d1d5db" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=F59E0B&text_color=d1d5db" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-F59E0B?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-F59E0B?style=for-the-badge&logo=linkedin&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["38-web3-nft.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=14,20&height=300&section=header&text=YOUR_NAME&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=42&desc=NFT+Developer+%7C+Digital+Artist&descAlignY=65" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Pacifico&size=24&pause=1000&color=E879F9&center=true&vCenter=true&width=700&lines=Minting+the+future+%F0%9F%8C%88;ERC-721+%7C+ERC-1155+%7C+EIP-2981;NFT+platforms+%7C+Generative+art;YOUR_TAGLINE" alt="NFT Typing"/>

---

### 🎨 NFT Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=solidity,ts,react,nodejs,ipfs,figma,python,git&perline=8"/>
</p>

**NFT Tools:** `OpenSea SDK` `Alchemy` `Moralis` `IPFS` `Arweave`  
**Standards:** `ERC-721` `ERC-1155` `EIP-2981` `ERC-2309`  
**Generative:** `p5.js` `Three.js` `Canvas API` `SVG`

---

### 🖼️ Collections

| Collection | Network | Items |
|------------|---------|-------|
| [YOUR_COLLECTION_1](https://opensea.io/collection/YOUR_COLLECTION_1) | Ethereum | 10k |
| [YOUR_COLLECTION_2](https://opensea.io/collection/YOUR_COLLECTION_2) | Polygon | 1k |

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dracula&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dracula&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-E879F9?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://opensea.io/YOUR_OPENSEA"><img src="https://img.shields.io/badge/OpenSea-E879F9?style=for-the-badge&logo=opensea&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=14,20&height=150&section=footer" width="100%"/>

</div>
"""

templates["39-web3-solidity.md"] = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Solidity+Developer+%7C+Smart+Contract+Engineer&descAlignY=60&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1000&color=627EEA&center=true&vCenter=true&width=700&lines=pragma+solidity+%5E0.8.0%3B;Building+trustless+systems+%F0%9F%94%92;Ethereum+%7C+Polygon+%7C+Arbitrum;YOUR_TAGLINE" alt="Solidity Typing"/>

---

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Developer {
    string public name = "YOUR_NAME";
    string public role = "Smart Contract Engineer";
    string public location = "YOUR_LOCATION";
    
    string[] public skills = [
        "Solidity", "EVM", "DeFi", "Security",
        "TypeScript", "Hardhat", "Foundry"
    ];
    
    function getContact() external pure returns (string memory) {
        return "YOUR_EMAIL";
    }
    
    function isAvailable() external pure returns (bool) {
        return true; // Open to work!
    }
}
```

---

### ⛓️ Chain Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=solidity,ts,js,react,nodejs,python,docker,git&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=ocean_dark&hide_border=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=ocean_dark&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-627EEA?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-627EEA?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["40-web3-multichain.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,17,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Multi-Chain+Developer+%7C+Web3+Builder&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=16&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&lines=Building+across+chains+%F0%9F%8C%89;ETH+%7C+SOL+%7C+COSMOS+%7C+POLKADOT;dApps+that+scale+%F0%9F%9A%80;YOUR_TAGLINE" alt="Multichain Typing"/>

---

### 🌉 Multi-Chain Presence

| Chain | Experience | Focus |
|-------|-----------|-------|
| Ethereum | ⭐⭐⭐⭐⭐ | DeFi, NFTs |
| Solana | ⭐⭐⭐⭐ | Programs, DeFi |
| Polygon | ⭐⭐⭐⭐ | Scaling, L2 |
| Cosmos | ⭐⭐⭐ | IBC, dApps |
| BNB Chain | ⭐⭐⭐ | dApps |

---

### 🛠 Web3 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=solidity,rust,ts,react,nodejs,python,docker,git&perline=8"/>
</p>

**Tools:** `Hardhat` `Foundry` `Anchor` `Ethers.js` `Viem` `CosmWasm`

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=nightowl&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=nightowl&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-38BDF8?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-38BDF8?style=for-the-badge&logo=linkedin&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,17,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["41-web3-dao.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=DAO+Builder+%7C+Governance+Architect&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=818CF8&center=true&vCenter=true&width=700&lines=Decentralizing+power+%F0%9F%97%B3%EF%B8%8F;DAO+governance+architect;Community-owned+protocols;YOUR_TAGLINE" alt="DAO Typing"/>

---

### 🏛️ Governance Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=solidity,ts,react,nodejs,postgres,ipfs,docker,git&perline=8"/>
</p>

**DAO Tools:** `OpenZeppelin Governor` `Gnosis Safe` `Snapshot` `Tally`  
**Token Standards:** `ERC-20` `ERC-721` `ERC-1155` `ERC-4626`

---

### 📊 Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=midnight-purple&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=midnight-purple&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-818CF8?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-818CF8?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>

</div>
"""

templates["42-web3-ethereum.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,14,9&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Ethereum+Developer+%7C+EVM+Expert&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1000&color=627EEA&center=true&vCenter=true&width=700&lines=Building+on+Ethereum+since+YOUR_YEAR;EVM+deep+diver+%F0%9F%94%8D;Security+%7C+Optimization+%7C+Protocols;YOUR_TAGLINE" alt="ETH Typing"/>

---

### Ξ Ethereum Expertise

```
Security:      ████████████████████ 100%
Gas Opt:       ███████████████░░░░░  75%
DeFi:          ████████████████░░░░  80%
NFTs:          ████████████░░░░░░░░  60%
Layer 2:       █████████████░░░░░░░  65%
EIPs:          ████████████████░░░░  80%
```

---

### ⚙️ Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=solidity,ts,react,nodejs,python,docker,hardhat,git&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dark&hide_border=true&bg_color=0d0d0d&title_color=627EEA&icon_color=627EEA&text_color=d1d5db" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=dark&hide_border=true&background=0d0d0d&ring=627EEA&fire=627EEA&currStreakLabel=627EEA" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-627EEA?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-627EEA?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20,14,9&height=100&section=footer" width="100%"/>

</div>
"""

# ─────────────────────────────────────────────────────────────
# PROFESSIONAL TEMPLATES (43-48)
# ─────────────────────────────────────────────────────────────

templates["43-professional-recruiter.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,14&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=YOUR_TITLE+%7C+YOUR_COMPANY&descAlignY=60&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Raleway&weight=600&size=20&pause=2000&color=3B82F6&center=true&vCenter=true&width=700&lines=YOUR_YEARS%2B+years+of+experience+%F0%9F%92%BC;Open+to+opportunities+%7C+YOUR_LOCATION;YOUR_TAGLINE" alt="Professional Typing"/>

---

### 💼 Professional Summary

> YOUR_PROFESSIONAL_SUMMARY — a brief 2-3 sentence overview of your experience, specialties, and what makes you stand out.

---

### 🛠 Core Competencies

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,python,postgres,docker,aws&perline=8"/>
</p>

| Domain | Technologies |
|--------|-------------|
| Frontend | React, Next.js, TypeScript, Tailwind |
| Backend | Node.js, Python, Go, GraphQL |
| Database | PostgreSQL, MongoDB, Redis |
| Cloud | AWS, GCP, Docker, Kubernetes |

---

### 📈 Impact

- 🚀 Led team of **YOUR_TEAM_SIZE** engineers
- 💰 Delivered **YOUR_REVENUE** in business value
- ⚡ Improved performance by **YOUR_PERF_GAIN%**
- 👥 Mentored **YOUR_MENTEE_COUNT** junior developers

---

### 📊 GitHub Activity

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=default&hide_border=false&title_color=3B82F6&icon_color=3B82F6" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=default&hide_border=false" height="155"/>
</p>

---

### 📬 Contact

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-3B82F6?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="https://YOUR_RESUME_URL"><img src="https://img.shields.io/badge/Resume-34D399?style=for-the-badge&logo=read-the-docs&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,14&height=100&section=footer" width="100%"/>

</div>
"""

templates["44-professional-engineer.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,9,14,17&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Senior+Software+Engineer+%7C+YOUR_COMPANY&descAlignY=60&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=20&pause=2000&color=6366F1&center=true&vCenter=true&width=700&lines=Building+scalable+systems+%F0%9F%8F%97;YOUR_YEARS%2B+years+shipping+code;YOUR_COMPANY+%7C+YOUR_PREV_COMPANY;YOUR_TAGLINE" alt="Engineer Typing"/>

---

<table>
<tr>
<td width="60%">

### 🏗️ About

- 🏢 **Company:** YOUR_COMPANY
- 📍 **Location:** YOUR_LOCATION  
- 💼 **Title:** YOUR_TITLE
- 🎓 **Education:** YOUR_DEGREE, YOUR_UNIVERSITY
- 🌱 **Currently:** YOUR_CURRENT_FOCUS
- 📫 **Email:** YOUR_EMAIL

</td>
<td width="40%">

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true" height="175"/>

</td>
</tr>
</table>

---

### ⚙️ Technical Expertise

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,nodejs,python,go,java&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=postgres,mongodb,redis,kafka,docker,kubernetes,aws,terraform&perline=8"/>
</p>

---

### 📊 Activity

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=tokyonight&hide_border=true" width="50%"/>
</p>

[![Activity](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=tokyo-night&hide_border=true)](https://github.com/YOUR_USERNAME)

---

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-6366F1?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-6366F1?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-6366F1?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,9,14,17&height=100&section=footer" width="100%"/>

</div>
"""

templates["45-professional-portfolio.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9&height=220&section=header&text=YOUR_NAME&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=YOUR_TITLE&descAlignY=60&descSize=24" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Lato&weight=700&size=20&pause=2000&color=0EA5E9&center=true&vCenter=true&width=700&lines=YOUR_TAGLINE_1;YOUR_TAGLINE_2;Available+for+freelance+%7C+full-time" alt="Portfolio Typing"/>

---

### 🚀 Featured Projects

<table>
<tr>
<td width="50%">
<h3 align="center">YOUR_PROJECT_1</h3>
<div align="center">
<a href="https://github.com/YOUR_USERNAME/YOUR_PROJECT_1" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_1&theme=transparent&hide_border=true&title_color=0EA5E9&text_color=94A3B8"/></a>
<br/><br/>
<a href="https://github.com/YOUR_USERNAME/YOUR_PROJECT_1"><img src="https://img.shields.io/badge/Code-0EA5E9?style=flat-square&logo=github&logoColor=white"/></a>
<a href="https://YOUR_PROJECT_1_DEMO"><img src="https://img.shields.io/badge/Live-10B981?style=flat-square&logo=vercel&logoColor=white"/></a>
</div>
</td>
<td width="50%">
<h3 align="center">YOUR_PROJECT_2</h3>
<div align="center">
<a href="https://github.com/YOUR_USERNAME/YOUR_PROJECT_2" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=YOUR_USERNAME&repo=YOUR_PROJECT_2&theme=transparent&hide_border=true&title_color=0EA5E9&text_color=94A3B8"/></a>
<br/><br/>
<a href="https://github.com/YOUR_USERNAME/YOUR_PROJECT_2"><img src="https://img.shields.io/badge/Code-0EA5E9?style=flat-square&logo=github&logoColor=white"/></a>
<a href="https://YOUR_PROJECT_2_DEMO"><img src="https://img.shields.io/badge/Live-10B981?style=flat-square&logo=vercel&logoColor=white"/></a>
</div>
</td>
</tr>
</table>

---

### 🛠 Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,python,postgres,docker,aws&perline=8"/>
</p>

---

### 📊 Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=0EA5E9&icon_color=0EA5E9&text_color=94A3B8" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=transparent&hide_border=true&ring=0EA5E9&fire=0EA5E9&currStreakLabel=0EA5E9" height="155"/>
</p>

---

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Portfolio-0EA5E9?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Hire Me-10B981?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9&height=100&section=footer" width="100%"/>

</div>
"""

templates["46-professional-consultant.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,6,14&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Tech+Consultant+%7C+YOUR_SPECIALTY&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Georgia&size=20&pause=2000&color=64748B&center=true&vCenter=true&width=700&lines=Helping+companies+build+better+software;YOUR_YEARS%2B+years+in+tech+consulting;YOUR_CLIENT_COUNT%2B+clients+served;YOUR_TAGLINE" alt="Consultant Typing"/>

---

### 💼 Services

| Service | Description |
|---------|-------------|
| 🏗️ Architecture Review | Assess and improve system design |
| 🚀 Technical Strategy | Roadmap planning and tech choices |
| 👥 Team Augmentation | Embedded engineering support |
| 📋 Code Audits | Quality, security, performance |
| 🎓 Training | Workshops for dev teams |

---

### 🤝 Clients & Industries

`FinTech` `HealthTech` `E-commerce` `SaaS` `Enterprise`

**Notable work with:** YOUR_CLIENT_1, YOUR_CLIENT_2, YOUR_CLIENT_3

---

### 🛠 Expertise

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nodejs,python,postgres,docker,aws,kubernetes&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=default&hide_border=false" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=default&hide_border=false" height="155"/>
</p>

---

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://YOUR_WEBSITE"><img src="https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Hire Me-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,6,14&height=100&section=footer" width="100%"/>

</div>
"""

templates["47-professional-leader.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9,14&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Engineering+Leader+%7C+YOUR_COMPANY&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Merriweather&size=18&pause=2000&color=7C3AED&center=true&vCenter=true&width=700&lines=Leading+teams%2C+shipping+products;Empowering+engineers+to+do+their+best;Tech+%2B+People+%2B+Strategy;YOUR_TAGLINE" alt="Leader Typing"/>

---

### 👥 Leadership Philosophy

> *"YOUR_LEADERSHIP_QUOTE"*

I believe in **YOUR_LEADERSHIP_PRINCIPLE_1**, **YOUR_LEADERSHIP_PRINCIPLE_2**, and **YOUR_LEADERSHIP_PRINCIPLE_3**.

---

### 🏆 Leadership Metrics

| Metric | Value |
|--------|-------|
| 👥 Team Size | YOUR_TEAM_SIZE engineers |
| 🚀 Products Shipped | YOUR_PRODUCTS |
| 📈 Revenue Impact | YOUR_REVENUE |
| 🌱 Engineers Grown | YOUR_PROMOTIONS promotions |

---

### 🛠 Technical Background

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nodejs,python,aws,docker,kubernetes,terraform&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true" height="155"/>
</p>

---

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-7C3AED?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://YOUR_BLOG"><img src="https://img.shields.io/badge/Blog-7C3AED?style=for-the-badge&logo=medium&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9,14&height=100&section=footer" width="100%"/>

</div>
"""

templates["48-professional-executive.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3a5f,100:0d6efd&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=CTO+%7C+VP+Engineering+%7C+Tech+Executive&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Merriweather&size=18&pause=3000&color=0D6EFD&center=true&vCenter=true&width=700&lines=YOUR_YEARS%2B+years+in+technology;From+IC+to+executive;Building+world-class+engineering+orgs;YOUR_TAGLINE" alt="Executive Typing"/>

---

### 📋 Executive Profile

| | |
|:--|:--|
| 🏢 **Current Role** | YOUR_TITLE @ YOUR_COMPANY |
| 🎓 **Education** | YOUR_DEGREE, YOUR_UNIVERSITY |
| 📍 **Location** | YOUR_LOCATION |
| 🌐 **LinkedIn** | [YOUR_NAME](https://linkedin.com/in/YOUR_LINKEDIN) |
| ✍️ **Writing** | [YOUR_BLOG](https://YOUR_BLOG) |
| 📧 **Contact** | YOUR_EMAIL |

---

### 🎯 Areas of Focus

- 🏗️ Engineering organization design & scaling
- 🚀 Product-engineering collaboration
- 🤖 AI/ML strategy and implementation
- 🌍 Remote-first team building
- 📈 Technical due diligence

---

### 📊 GitHub (IC days)

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=default&hide_border=false&title_color=0D6EFD" height="155"/>
</p>

---

<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://YOUR_BLOG"><img src="https://img.shields.io/badge/Newsletter-0D6EFD?style=for-the-badge&logo=substack&logoColor=white"/></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3a5f,100:0d6efd&height=100&section=footer" width="100%"/>

</div>
"""

# ─────────────────────────────────────────────────────────────
# SPECIALTY / BONUS TEMPLATES (49-56)
# ─────────────────────────────────────────────────────────────

templates["49-devops-sre.md"] = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,20,24&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=DevOps+Engineer+%7C+SRE+%7C+Platform+Eng&descAlignY=60&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1000&color=22D3EE&center=true&vCenter=true&width=700&lines=kubectl+get+pods+--all-namespaces;terraform+apply+✅;99.99%25+uptime+or+bust+%F0%9F%9A%80;YOUR_TAGLINE" alt="DevOps Typing"/>

---

### ☁️ Infrastructure Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=aws,gcp,azure,docker,kubernetes,terraform,ansible,helm&perline=8"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=python,bash,go,prometheus,grafana,jenkins,git,linux&perline=8"/>
</p>

---

### 📈 SRE Metrics

```
⬆️  AVAILABILITY:  99.99%
⚡  MTTR:           < 5 min
🚀  DEPLOY FREQ:    50+ deploys/day
🔒  INCIDENTS:      0 P0 this month
📊  OBSERVABILITY:  100% coverage
```

---

### 🛠 Certifications

<p align="center">
  <img src="https://img.shields.io/badge/AWS-Solutions Architect-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white"/>
  <img src="https://img.shields.io/badge/CKA-Certified-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white"/>
  <img src="https://img.shields.io/badge/Terraform-Associate-7B42BC?style=for-the-badge&logo=terraform&logoColor=white"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=ocean_dark&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=ocean_dark&hide_border=true" height="155"/>
</p>

---

<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-22D3EE?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-22D3EE?style=for-the-badge&logo=twitter&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=14,20,24&height=100&section=footer" width="100%"/>

</div>
"""

templates["50-mobile-dev.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Mobile+Developer+%7C+iOS+%2B+Android&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=34D399&center=true&vCenter=true&width=700&lines=Building+apps+people+use+every+day+%F0%9F%93%B1;Swift+%7C+Kotlin+%7C+React+Native+%7C+Flutter;YOUR_APP_DOWNLOADS%2B+downloads;YOUR_TAGLINE" alt="Mobile Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212748830-4c709398-a386-4761-84d7-9e10b98fbe6e.gif" width="300"/>

---

### 📱 Mobile Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=swift,kotlin,react,flutter,ts,firebase,figma,git&perline=8"/>
</p>

| Platform | Framework | Experience |
|----------|-----------|------------|
| iOS | Swift / SwiftUI | YOUR_YEARS yrs |
| Android | Kotlin / Compose | YOUR_YEARS yrs |
| Cross-platform | React Native | YOUR_YEARS yrs |
| Cross-platform | Flutter | YOUR_YEARS yrs |

---

### 📊 App Store Highlights

<p align="center">
  <img src="https://img.shields.io/badge/App Store-000000?style=for-the-badge&logo=apple&logoColor=white"/>
  <img src="https://img.shields.io/badge/Play Store-414141?style=for-the-badge&logo=google-play&logoColor=white"/>
  <img src="https://img.shields.io/badge/Downloads-YOUR_COUNT%2B-34D399?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Rating-★ YOUR_RATING-yellow?style=for-the-badge"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=vue-dark&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=vue-dark&hide_border=true" height="155"/>
</p>

---

<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-34D399?style=for-the-badge&logo=linkedin&logoColor=black"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-34D399?style=for-the-badge&logo=twitter&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["51-security-researcher.md"] = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=00FF41&animation=twinkling&fontAlignY=38&desc=Security+Researcher+%7C+Bug+Bounty+Hunter&descAlignY=60&descFontColor=00FF41" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Source+Code+Pro&size=18&pause=1000&color=00FF41&center=true&vCenter=true&width=700&lines=%24+nmap+-sV+target.com;%24+sqlmap+-u+%22https%3A%2F%2Ftarget.com%22;Ethical+hacker+%7C+CTF+player+%F0%9F%9A%A9;YOUR_CVE_COUNT%2B+CVEs+disclosed" alt="Security Typing"/>

---

### 🔒 Security Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,bash,linux,docker,git,kali,burpsuite,metasploit&perline=8"/>
</p>

**Tools:** `Burp Suite` `Metasploit` `Nmap` `Wireshark` `OWASP ZAP`  
**Areas:** `Web AppSec` `Network Security` `Reverse Engineering` `Malware Analysis`

---

### 🏆 Bug Bounty Hall of Fame

| Platform | Rank | Reports |
|----------|------|---------|
| HackerOne | YOUR_RANK | YOUR_REPORTS |
| Bugcrowd | YOUR_RANK | YOUR_REPORTS |
| YOUR_PROGRAM | YOUR_RANK | YOUR_REPORTS |

---

### 🚩 CTF Achievements

<p align="center">
  <img src="https://img.shields.io/badge/CTFtime-Rating YOUR_RATING-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Hack The Box-YOUR_RANK-9FEF00?style=for-the-badge&logo=hackthebox&logoColor=black"/>
  <img src="https://img.shields.io/badge/TryHackMe-YOUR_RANK-red?style=for-the-badge&logo=tryhackme&logoColor=white"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=merko&hide_border=true&bg_color=0a0a0a&title_color=00FF41&icon_color=00FF41&text_color=00cc33" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-00FF41?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-00FF41?style=for-the-badge&logo=linkedin&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=9,14,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["52-gaming-dev.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,17,20&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Game+Developer+%7C+YOUR_ENGINE+%7C+YOUR_GENRE&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=14&pause=1000&color=F59E0B&center=true&vCenter=true&width=700&lines=PLAYER+ONE+READY...;Loading+YOUR_NAME...;LEVEL+UP+%F0%9F%8E%AE;INSERT+COIN+TO+CONTINUE" alt="Gaming Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212748842-9fcbad5b-6173-4175-8a61-521f3dbb7514.gif" width="300"/>

---

```
╔══ GAME DEV PROFILE ═══════════════════════════════╗
║                                                    ║
║  PLAYER: YOUR_NAME                                 ║
║  CLASS:  Game Developer                            ║
║  EXP:    YOUR_YEARS years                          ║
║  LEVEL:  YOUR_LEVEL                                ║
║  HP:     ████████████ 100%                         ║
║  MANA:   ████████████ (Coffee)                     ║
║                                                    ║
║  SKILLS:                                           ║
║  ▸ Unity       [████████████]                      ║
║  ▸ C#          [██████████░░]                      ║
║  ▸ C++         [████████░░░░]                      ║
║  ▸ Unreal      [██████░░░░░░]                      ║
║  ▸ Godot       [████░░░░░░░░]                      ║
║                                                    ║
╚════════════════════════════════════════════════════╝
```

---

### 🎮 Games Shipped

| Game | Engine | Platform | Players |
|------|--------|----------|---------|
| YOUR_GAME_1 | YOUR_ENGINE | YOUR_PLATFORM | YOUR_PLAYERS |
| YOUR_GAME_2 | YOUR_ENGINE | YOUR_PLATFORM | YOUR_PLAYERS |

---

### 🛠 Dev Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=unity,cs,cpp,python,blender,git,github,vscode&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=solarized-dark&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=solarized-dark&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-F59E0B?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://itch.io/YOUR_ITCHIO"><img src="https://img.shields.io/badge/itch.io-FA5C5C?style=for-the-badge&logo=itch.io&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-F59E0B?style=for-the-badge&logo=linkedin&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,17,20&height=100&section=footer" width="100%"/>

</div>
"""

templates["53-ux-ui-designer.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=UX%2FUI+Designer+%7C+Design+Engineer&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Nunito&weight=700&size=22&pause=1200&color=F472B6&center=true&vCenter=true&width=700&lines=Design+is+not+just+what+it+looks+like...;...design+is+how+it+works+🎨;Bridging+design+%26+code+since+YOUR_YEAR;YOUR_TAGLINE" alt="Design Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="250"/>

---

### 🎨 Design Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=figma,xd,ps,ai,html,css,js,react&perline=8"/>
</p>

**Design Tools:** `Figma` `Adobe XD` `Photoshop` `Illustrator` `Framer`  
**Prototyping:** `InVision` `Marvel` `Principle` `ProtoPie`  
**Code:** `HTML/CSS` `React` `Tailwind` `Framer Motion`

---

### 🖼️ Design Work

| Project | Type | Link |
|---------|------|------|
| YOUR_DESIGN_1 | Web App | [Figma](https://YOUR_FIGMA_1) |
| YOUR_DESIGN_2 | Mobile | [Behance](https://YOUR_BEHANCE_1) |
| YOUR_DESIGN_3 | Branding | [Dribbble](https://YOUR_DRIBBBLE_1) |

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=swift&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=swift&hide_border=true" height="155"/>
</p>

---

<a href="https://dribbble.com/YOUR_DRIBBBLE"><img src="https://img.shields.io/badge/Dribbble-F472B6?style=for-the-badge&logo=dribbble&logoColor=white"/></a>
<a href="https://behance.net/YOUR_BEHANCE"><img src="https://img.shields.io/badge/Behance-F472B6?style=for-the-badge&logo=behance&logoColor=white"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-F472B6?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6&height=100&section=footer" width="100%"/>

</div>
"""

templates["54-indie-hacker.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,17&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Indie+Hacker+%7C+Solo+Builder+%7C+YOUR_MRR+MRR&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=FBBF24&center=true&vCenter=true&width=700&lines=Building+in+public+%F0%9F%93%A2;YOUR_PRODUCT_COUNT%2B+shipped+products;From+0+to+MRR+%F0%9F%9A%80;YOUR_TAGLINE" alt="Indie Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100"/>

---

### 🚀 Products

| Product | Description | MRR | Status |
|---------|-------------|-----|--------|
| [YOUR_PRODUCT_1](https://YOUR_PRODUCT_1_URL) | YOUR_DESC_1 | $YOUR_MRR_1 | 🟢 Live |
| [YOUR_PRODUCT_2](https://YOUR_PRODUCT_2_URL) | YOUR_DESC_2 | $YOUR_MRR_2 | 🟡 Beta |
| [YOUR_PRODUCT_3](https://YOUR_PRODUCT_3_URL) | YOUR_DESC_3 | — | 🔵 Building |

---

### ⚡ Ship Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,postgres,stripe,vercel,git&perline=8"/>
</p>

---

### 📈 Revenue Journey

```
Month 1:  $0
Month 3:  $YOUR_3M_MRR
Month 6:  $YOUR_6M_MRR
Month 12: $YOUR_12M_MRR
Today:    $YOUR_CURRENT_MRR 🎉
```

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical&hide_border=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=radical&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FBBF24?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://YOUR_BLOG"><img src="https://img.shields.io/badge/Newsletter-FBBF24?style=for-the-badge&logo=substack&logoColor=black"/></a>
<a href="https://producthunt.com/@YOUR_PH"><img src="https://img.shields.io/badge/Product Hunt-FBBF24?style=for-the-badge&logo=product-hunt&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=5,12,17&height=100&section=footer" width="100%"/>

</div>
"""

templates["55-content-creator.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9,14&height=200&section=header&text=YOUR_NAME&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Developer+%7C+Content+Creator+%7C+Educator&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Nunito&weight=700&size=20&pause=1000&color=EF4444&center=true&vCenter=true&width=700&lines=Teaching+coding+to+YOUR_FOLLOWERS%2B+people+%F0%9F%8E%93;YouTube+%7C+Twitter+%7C+Blog;Making+tech+accessible+%F0%9F%9A%80;YOUR_TAGLINE" alt="Creator Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="700"/>

---

### 📺 Content Stats

<p align="center">
  <img src="https://img.shields.io/badge/YouTube-YOUR_SUBS Subs-FF0000?style=for-the-badge&logo=youtube&logoColor=white"/>
  <img src="https://img.shields.io/badge/Twitter-YOUR_FOLLOWERS Followers-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Newsletter-YOUR_SUBSCRIBERS Subscribers-FF6719?style=for-the-badge&logo=substack&logoColor=white"/>
  <img src="https://img.shields.io/badge/Blog-YOUR_VIEWS Views-000000?style=for-the-badge&logo=medium&logoColor=white"/>
</p>

---

### 🎥 Latest Content

| Title | Platform | Views |
|-------|----------|-------|
| [YOUR_VIDEO_1](https://YOUR_VIDEO_1_URL) | YouTube | YOUR_VIEWS |
| [YOUR_ARTICLE_1](https://YOUR_ARTICLE_1_URL) | Blog | YOUR_READS |
| [YOUR_THREAD_1](https://twitter.com/YOUR_TWITTER) | Twitter | YOUR_IMPRESSIONS |

---

### 🛠 Teaching Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,python,docker,git,vscode&perline=8"/>
</p>

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight&hide_border=true" height="155"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=tokyonight&hide_border=true" height="155"/>
</p>

---

<a href="https://youtube.com/@YOUR_YOUTUBE"><img src="https://img.shields.io/badge/YouTube-EF4444?style=for-the-badge&logo=youtube&logoColor=white"/></a>
<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://YOUR_BLOG"><img src="https://img.shields.io/badge/Newsletter-FF6719?style=for-the-badge&logo=substack&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,6,9,14&height=100&section=footer" width="100%"/>

</div>
"""

templates["56-hackathon-champion.md"] = """<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5,2&height=220&section=header&text=YOUR_NAME&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=38&desc=%F0%9F%8F%86+Hackathon+Champion+%7C+YOUR_ROLE&descAlignY=60" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=18&pause=1000&color=FBBF24&center=true&vCenter=true&width=700&lines=YOUR_WIN_COUNT%2B+hackathon+wins+%F0%9F%8F%86;48+hours+%3D+infinite+possibilities;Ship+or+go+home+%F0%9F%9A%80;YOUR_TAGLINE" alt="Champion Typing"/>

<img src="https://user-images.githubusercontent.com/74038190/216644497-1951db19-8f3d-4e44-ac08-8e9d7e0d94a7.gif" width="150"/>

---

### 🏅 Trophy Case

| 🥇 Event | 🚀 Project | 💰 Prize |
|---------|----------|---------|
| YOUR_HACKATHON_1 | [YOUR_PROJECT_1](https://github.com/YOUR_USERNAME/YOUR_PROJECT_1) | $YOUR_PRIZE_1 |
| YOUR_HACKATHON_2 | [YOUR_PROJECT_2](https://github.com/YOUR_USERNAME/YOUR_PROJECT_2) | $YOUR_PRIZE_2 |
| YOUR_HACKATHON_3 | [YOUR_PROJECT_3](https://github.com/YOUR_USERNAME/YOUR_PROJECT_3) | $YOUR_PRIZE_3 |
| YOUR_HACKATHON_4 | [YOUR_PROJECT_4](https://github.com/YOUR_USERNAME/YOUR_PROJECT_4) | $YOUR_PRIZE_4 |

---

### ⚡ Hackathon Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,nodejs,openai,supabase,vercel,figma&perline=8"/>
</p>

**Favorites:** `Next.js` + `Supabase` + `OpenAI` = shipped in 8h ⚡

---

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=radical&no-frame=true&row=1&column=8"/>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical&hide_border=true" height="155"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=YOUR_USERNAME&theme=radical&hide_border=true" height="155"/>
</p>

---

<a href="https://twitter.com/YOUR_TWITTER"><img src="https://img.shields.io/badge/Twitter-FBBF24?style=for-the-badge&logo=twitter&logoColor=black"/></a>
<a href="https://devpost.com/YOUR_DEVPOST"><img src="https://img.shields.io/badge/Devpost-FBBF24?style=for-the-badge&logo=devpost&logoColor=black"/></a>
<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-FBBF24?style=for-the-badge&logo=linkedin&logoColor=black"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5,2&height=100&section=footer" width="100%"/>

</div>
"""

# Write all files
for filename, content in templates.items():
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print(f"✅ Generated {len(templates)} templates")
for fname in sorted(templates.keys()):
    print(f"  • {fname}")