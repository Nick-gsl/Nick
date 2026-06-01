# 🔥 地狱死神 DJ 舞曲 + MV 提示词库

> 工作流：Suno（音乐）→ GPT-Image（缩略图 + 分镜图）→ Veo3（分镜视频）
> 风格定位：劲爆混合DJ舞曲 / 纯器乐 / 10分钟长曲 / 16:9 / 恐怖惊悚 / 地狱死神

---

## 🎨 第 0 步：先生成本期「配色方案」（每期换一套）

每做一期视频，先用下面这段去问 ChatGPT（文字），让它给你一套统一配色，
然后把结果（主色 / 辅色 / 点缀色 + 英文色值）填进后面所有图像和视频提示词里，
保证**缩略图、分镜、视频全程配色统一**。

```
你是恐怖暗黑视觉的美术指导。请为一支"地狱死神主题的劲爆DJ舞曲"视频，
推荐 1 套恐怖惊悚风格的配色方案，要求：强对比、高冲击力、适合发光特效。
输出格式：
- 主色（含英文+大致色值）
- 辅色
- 点缀/发光色
- 一句话氛围描述
请直接给我一套，不要解释过程。
```

**备选配色（懒得问AI时直接挑一个）：**
| 编号 | 配色 | 氛围 |
|------|------|------|
| A | 岩浆红黑 (crimson + black + molten orange) | 地狱熔炉，最经典 |
| B | 鬼火青绿 (toxic green + deep black + acid lime) | 阴森幽灵感 |
| C | 暗能量紫 (electric purple + black + magenta glow) | 神秘暗黑 |
| D | 冰冷死神蓝 (icy cyan + black + electric blue) | 寒冷诡异 |
| E | 血月橙红 (blood orange + charcoal + ember red) | 末日战歌 |

> 后文所有提示词里出现 `【主色】`、`【辅色】`、`【点缀色】` 的地方，替换成本期方案即可。

---

## 🎵 一、Suno 音乐提示词（纯器乐 / 混合DJ / 10分钟）

### Suno 设置
- **打开 Instrumental（纯器乐）开关**
- 风格框（Style）填下面的描述，标题随意
- 10分钟做法：先生成一段主曲（v4.5+ 单段约 4 分钟），再用 **Extend（续写）** 接 2~3 次，最后导出拼成 10 分钟连续混音

### ① 通用劲爆混合风格（推荐主用）
```
dark phonk x hardstyle x big room techno fusion, aggressive festival rave banger,
distorted 808 bass, pounding four-on-the-floor kick, ominous horror synth leads,
demonic choir pads, cinematic build-ups and explosive drops, 150 BPM,
high energy, club destroyer, instrumental, no vocals
```

### ② 暗黑机车 Phonk 偏向
```
aggressive drift phonk, cowbell melody, heavy distorted 808, dark menacing atmosphere,
horror movie tension, hard-hitting drops, 145 BPM, instrumental, evil vibe
```

### ③ 硬核蹦迪 Hardstyle 偏向
```
euphoric hardstyle x rawstyle, reverse bass, distorted kicks, screeching leads,
epic dark orchestral intro, festival mainstage energy, 155 BPM, instrumental, intense
```

### ④ 末日大场面 Bigroom / Techno
```
dark big room techno, peak-time festival, massive drops, industrial percussion,
apocalyptic atmosphere, tension risers, sirens, 150 BPM, instrumental, powerful
```

### 结构标签（贴在歌词框里控制段落，做出DJ起伏）
```
[Intro] dark ambient horror pad, distant bell toll, eerie tension
[Build-Up] rising snare roll, riser sweep, building suspense
[Drop] explosive distorted bass, aggressive lead, full energy
[Break] stripped beat, haunting melody, breathing room
[Build-Up 2] faster snare roll, white noise riser
[Drop 2] heavier drop, layered synths, maximum impact
[Outro] fading reverb, lingering dark pad
```

> 💡 想要每段风格不同（真正"混合"），可以分别用①②③④各生成一段，再拼接，曲风切换更明显。

---

## 🖼️ 二、GPT-Image 缩略图提示词（16:9 / 地狱死神 / 恐怖）

### 万能模板（替换【】内容即可）
```
A terrifying Grim Reaper as a DJ, hooded skeletal figure with glowing eyes,
standing behind a massive demonic DJ booth, raising a scythe like a hand in the air,
hellfire and embers exploding around, dark smoke, cracked ground with lava veins,
horror movie poster style, ultra dramatic lighting, cinematic, hyper-detailed,
color palette: 【主色】 dominant, 【辅色】 background, 【点缀色】 glowing accents,
high contrast, ominous and intense, 16:9, 8k, thumbnail composition with empty
space top-left for title text
```

### 现成方案（直接抄）

**A. 岩浆红黑·地狱DJ台**
```
A menacing Grim Reaper DJ in a black tattered cloak, skull face with glowing crimson
eyes, hands on glowing turntables made of bone and fire, erupting volcano of lava
behind, floating fire embers, molten cracks on the ground, intense crimson and orange
hellfire lighting against pure black, horror poster, cinematic, hyper-detailed, 16:9,
strong contrast, leave empty dark space at top for title
```

**B. 鬼火青绿·幽灵蹦迪**
```
A ghostly Grim Reaper raising both skeletal arms, surrounded by swirling toxic green
flames and floating skulls, neon acid-green glow against deep black void, eerie fog,
horror movie key art, dramatic rim lighting, hyper-detailed, ominous, 16:9, cinematic,
negative space for thumbnail text
```

**C. 暗能量紫·恶魔仪式**
```
Close-up of a hooded Grim Reaper, electric purple energy and magenta lightning
crackling around the hood, glowing eyes, dark cathedral ruins in background,
purple-black color grade with magenta glow accents, terrifying, cinematic horror
poster, hyper-detailed, 16:9, high contrast, space for bold title text
```

> 关键词作用：`horror poster / cinematic / high contrast / glowing eyes / hellfire` 决定恐怖感；
> `empty space / negative space for title` 是给你留出加标题文字的位置；
> 如果想让AI自己定配色，把配色那行换成：`dramatic horror color grading, AI-chosen striking palette`。

---

## 🎬 三、MV 分镜「生成器」（每期重新生成 + CSV 输出）

> ⚠️ 核心思路：**分镜不要写死**。每期做新歌时，用下面的「分镜生成器」让 AI
> 根据本期曲风 / BPM / 段落结构 / 配色，**现场生成一批全新的、贴合这首歌的分镜**，
> 并以 **CSV 格式**输出，方便你导入表格 / Excel / Notion 批量管理。
> 后面的「镜头点子库」只是灵感参考，不是固定清单。

### 3.1 固定视觉锚点（这部分写死，保证系列一致性）

每期生成分镜都必须遵守，让"死神"和画风跨期统一：

```
主角：The Grim Reaper（地狱死神）—— 黑色破烂兜帽长袍 hooded skeletal figure,
glowing eyes, tattered black cloak flowing like smoke
画风：恐怖惊悚 horror, 抽象超现实 abstract surreal, 电影感 cinematic,
hyper-detailed, dramatic lighting
画幅：16:9
配色：本期统一配色（替换 【主色】/【辅色】/【点缀色】）
禁止：可爱卡通、明亮日常、文字水印
```

### 3.2 分镜生成器（每期复制这段，填空后丢给 ChatGPT）

```
你是恐怖暗黑 MV 的分镜导演。请为一支【地狱死神主题的劲爆DJ舞曲】MV 生成分镜表。

【本期歌曲信息】（我来填）
- 曲风：________（如 dark phonk / hardstyle / bigroom，可多种混合）
- BPM：________
- 时长：约 10 分钟
- 段落结构：________（如 Intro→Build→Drop→Break→Drop2→Outro，按你的曲子填）
- 本期配色：主色 ________ / 辅色 ________ / 点缀色 ________

【固定视觉锚点】
主角死神：hooded skeletal Grim Reaper, glowing eyes, tattered black cloak。
画风：horror, abstract surreal, cinematic, hyper-detailed, 16:9。
全程使用本期配色，禁止可爱/明亮/文字水印。

【要求】
1. 生成 22 个不重复的分镜，覆盖整首歌的情绪起伏。
2. 按段落分配：Intro/Break 用铺垫与抽象转场镜头，Drop 用炸点/高潮镜头。
3. 必须包含「死神跳舞」相关的核心抽象镜头至少 3 个（这是频道记忆点）。
4. 每个镜头的英文提示词都要把配色词填进去（不要留占位符），结尾固定带
   "cinematic horror, hyper-detailed, 16:9"。
5. 镜头要有变化：登场/特写/群舞/转场/漩涡/机车/王座/爆炸等，别全是同一种。

【输出格式：严格输出 CSV，第一行为表头，逗号分隔，英文提示词字段用双引号包裹】
shot_id,section,beat_cue,scene_cn,image_prompt_en,shot_type,motion_hint
说明：
- shot_id：镜头序号 1~22
- section：所属段落（Intro/Build/Drop/Break/Drop2/Outro）
- beat_cue：建议出现的大致时间或卡点（如 0:00-0:30 / Drop1）
- scene_cn：一句话中文画面描述
- image_prompt_en：GPT-Image 用的完整英文提示词（含本期配色，已填好）
- shot_type：镜头类型（WS远景/MS中景/CU特写/POV主观/ABS抽象）
- motion_hint：给 Veo3 的运动提示（如 slow push in / orbit / shake to beat）

只输出 CSV，不要额外解释。
```

> 💡 用法：把上面这段复制给 ChatGPT，填好歌曲信息 → 它直接吐一份 CSV →
> 你存成 `.csv` 用 Excel/表格打开，`image_prompt_en` 列逐个喂 GPT-Image 出图，
> `motion_hint` 列后面喂 Veo3。每期歌不同 → 分镜也不同，但死神和配色始终统一。

### 3.3 CSV 输出示例（生成器会产出这样的内容）

```csv
shot_id,section,beat_cue,scene_cn,image_prompt_en,shot_type,motion_hint
1,Intro,0:00-0:30,死神在浓雾中登场,"Wide cinematic shot, a towering Grim Reaper silhouette emerging from thick dark fog, glowing eyes piercing through, embers floating, crimson and molten orange glow against black, surreal horror, cinematic horror, hyper-detailed, 16:9",WS,slow tilt up revealing figure
2,Build,0:30-1:00,骷髅手破土而出,"Skeletal hands erupting from cracked burning ground reaching to the sky, smoke and embers rising, crimson glow with molten orange accents, cinematic horror, hyper-detailed, 16:9",MS,hands rise slowly
6,Drop,1:00-1:30,死神随节奏跳舞,"A skeletal Grim Reaper dancing with rhythmic exaggerated poses, tattered cloak flowing like liquid smoke, swirling particles and neon trails, crimson and molten orange glow, cinematic horror, hyper-detailed, 16:9",ABS,sway and dance, push in
```

> 上面只是格式示范（用"岩浆红黑"配色填好的样子）。实际让生成器按你本期歌曲生成完整 22 行。

---

## 📎 附录 · 镜头点子库（没灵感时参考，不是固定清单）

> 下面 22 个是现成镜头点子，可以当生成器的"种子"，或直接挑几个用。
> 仍含 `【主色】/【辅色】/【点缀色】` 占位符，手动替换即可。

### 🟥 第一组 · 开场铺垫（镜头 1-5）

**镜头 1 · 死神登场**
```
Wide cinematic shot, a towering Grim Reaper silhouette emerging from thick dark fog,
glowing eyes piercing through, embers floating, abstract hellish background, color
palette 【主色】+【点缀色】, surreal horror, hyper-detailed, 16:9, atmospheric
```

**镜头 2 · 骷髅手破土**
```
Skeletal hands erupting from cracked burning ground, reaching toward the sky, smoke and
embers rising, dark abstract hell environment, 【主色】 glow with 【点缀色】 accents,
cinematic horror, hyper-detailed, 16:9, ominous
```

**镜头 3 · 死神睁眼特写**
```
Extreme close-up of the Grim Reaper's hood, two glowing eyes slowly igniting in the
darkness, faint smoke drifting, hell reflected in the pupils, 【点缀色】 glow against
black, terrifying, cinematic, hyper-detailed, 16:9
```

**镜头 4 · 火海中行走**
```
The Grim Reaper walking slowly through a sea of fire, cloak trailing flames, silhouette
against towering hellfire, abstract surreal scale, 【主色】 and 【点缀色】 lighting,
epic cinematic horror, 16:9, atmospheric
```

**镜头 5 · 巨型死神俯视城市**
```
A colossal Grim Reaper looming over a burning ruined city, glowing eyes, scythe in hand,
apocalyptic sky, abstract surreal scale, 【主色】 dominant with 【点缀色】 glow,
cinematic horror, hyper-detailed, 16:9, epic
```

### 🟧 第二组 · 核心炸点（镜头 6-12）

**镜头 6 · 死神跳舞（核心）**
```
A skeletal Grim Reaper dancing with rhythmic exaggerated poses, tattered cloak flowing
like liquid smoke, surrounded by swirling particles and neon energy trails, abstract
psychedelic background, motion blur, surreal, 【主色】 and 【点缀色】 glow, dramatic
lighting, 16:9, dynamic composition
```

**镜头 7 · 死神DJ打碟特写**
```
Close-up of the Grim Reaper's bony hands scratching glowing turntables made of bone and
fire, sound waves rippling out, sparks flying, dark abstract booth, 【主色】 and
【点缀色】 neon glow, cinematic, hyper-detailed, 16:9, high energy
```

**镜头 8 · 地狱之翼展开**
```
The Grim Reaper spreading massive flaming wings, embers exploding outward, glowing eyes,
abstract hell background, dramatic backlight, 【主色】 fire with 【点缀色】 accents,
epic cinematic horror, hyper-detailed, 16:9
```

**镜头 9 · 死神挥镰特写**
```
Dramatic close-up of the Grim Reaper swinging a glowing scythe, sparks and fire trailing
the blade, intense glowing eyes, dark abstract background with energy waves, 【主色】
lighting, cinematic horror, motion blur, 16:9
```

**镜头 10 · 死神召唤闪电**
```
The Grim Reaper raising both arms, summoning crackling energy and lightning from a
storming hell sky, glowing eyes, power surging around the body, abstract surreal,
【主色】 and 【点缀色】 electric glow, cinematic horror, hyper-detailed, 16:9
```

**镜头 11 · 死神骑机车（Phonk感）**
```
The Grim Reaper riding a flaming demonic motorcycle through a dark tunnel of fire, motion
blur, speed lines, sparks trailing, abstract phonk aesthetic, 【主色】 and 【点缀色】
neon glow, cinematic, hyper-detailed, 16:9, intense energy
```

**镜头 12 · 地狱舞池**
```
A demonic nightclub in hell, skeleton crowd raving, the Grim Reaper DJ on an elevated
booth of bones and fire, laser beams and embers, abstract chaotic energy, 【主色】 and
【点缀色】 neon, cinematic horror, 16:9, high energy
```

### 🟪 第三组 · 抽象转场（镜头 13-18）

**镜头 13 · 灵魂漩涡**
```
Abstract vortex of screaming ghost faces and souls spiraling into darkness, the Grim
Reaper at the center, swirling smoke and fire, surreal nightmare, 【主色】 and black,
【点缀色】 glow, hyper-detailed, 16:9, hypnotic
```

**镜头 14 · 万花筒死神**
```
Kaleidoscopic symmetrical pattern of multiplied Grim Reaper figures and skulls, trippy
psychedelic hell mandala, swirling fire and particles, 【主色】 dominant with 【点缀色】
accents, surreal abstract, hyper-detailed, 16:9, hypnotic
```

**镜头 15 · 死神破碎重组**
```
The Grim Reaper shattering into thousands of glowing particles and ash, then reforming,
abstract dispersion effect, dark void background, 【主色】 and 【点缀色】 glow, surreal,
cinematic, hyper-detailed, 16:9, dynamic
```

**镜头 16 · 漂浮头骨阵列**
```
An endless wall of floating screaming skulls receding into darkness, faint glow in the
eye sockets, drifting smoke, abstract surreal, 【主色】 and 【点缀色】 lighting, eerie,
cinematic horror, hyper-detailed, 16:9
```

**镜头 17 · 灵魂锁链**
```
Glowing chains of tormented souls swirling around the Grim Reaper, ghostly faces pulled
through smoke, abstract surreal hell, 【主色】 and 【点缀色】 glow against black,
cinematic horror, hyper-detailed, 16:9, ominous
```

**镜头 18 · 时间倒计时**
```
The Grim Reaper standing before a giant cracked glowing clock, sand and ash falling,
abstract surreal hell, dramatic lighting, 【主色】 dominant with 【点缀色】 glow,
cinematic horror, hyper-detailed, 16:9, ominous
```

### 🟨 第四组 · 高潮终场（镜头 19-22）

**镜头 19 · 抽象骷髅群舞**
```
Surreal scene of multiple glowing skeletons dancing in sync, abstract geometric hell
dimension, floating skulls and fire, kaleidoscopic symmetry, 【主色】 dominant with
【点缀色】 accents, trippy horror, hyper-detailed, 16:9
```

**镜头 20 · 双死神镜像对舞**
```
Two mirrored Grim Reapers dancing symmetrically face to face, cloaks flowing like smoke,
energy trails connecting them, abstract surreal background, 【主色】 and 【点缀色】 glow,
dramatic lighting, cinematic, hyper-detailed, 16:9, dynamic
```

**镜头 21 · 死神王座**
```
The Grim Reaper sitting on a towering throne of skulls and bones, fire burning behind,
glowing eyes, scythe resting beside, abstract epic hell hall, 【主色】 and 【点缀色】
lighting, cinematic horror, hyper-detailed, 16:9, majestic
```

**镜头 22 · 终场大爆炸**
```
The Grim Reaper raising both arms as everything erupts in a massive explosion of fire,
embers and energy, skeleton crowd below, abstract chaotic finale, 【主色】 and 【点缀色】
blast, epic cinematic horror, hyper-detailed, 16:9, maximum impact
```

> 这些只是**点子参考**。正式做片时请用 §3.2 的生成器，按本期歌曲重新生成贴合的分镜（CSV）。
> 想扩充点子，把"死神 + 一个动作 + 抽象环境 + 本期配色"自由组合即可。

---

## 📹 四、Veo3 视频提示词（图生视频 / 动态化分镜）

### 用法
把分镜图上传到 Veo3（图生视频），运动描述**直接用 CSV 里的 `motion_hint` 列**，
不够细就参考下面的模板补充。Veo3 单段约 8 秒，10分钟需要拼很多段。
建议每段都用慢动作 + 循环感强的运动，方便剪辑卡点。

> ⚠️ Veo3 默认会生成声音，做MV时把生成的音频**静音/丢弃**，统一用 Suno 的曲子。

### 运动提示词模板（CSV 的 motion_hint 不够时参考）

**死神跳舞（核心）**
```
The Grim Reaper sways and dances rhythmically to the beat, cloak billowing like smoke,
embers and particles floating upward, camera slowly pushes in, slow motion, dark
cinematic horror, looping motion
```

**死神登场**
```
Thick fog drifts as the Grim Reaper slowly steps forward, glowing eyes intensifying,
camera slowly tilts up to reveal full figure, embers rising, slow dramatic motion,
cinematic
```

**挥镰特写**
```
The Grim Reaper swings the glowing scythe in a slow arc, sparks trailing the blade,
slow motion, camera slight orbit, fire flickering, intense cinematic horror
```

**灵魂漩涡 / 转场**
```
The vortex of souls spirals and swirls hypnotically, ghost faces emerging and fading,
smoke rotating, camera slowly zooms into the center, surreal nightmare motion, seamless loop
```

**地狱舞池**
```
The skeleton crowd jumps and raves in rhythm, laser beams sweeping, embers raining,
the Reaper DJ raises an arm, fast energetic motion, camera shakes slightly to the beat,
cinematic, high energy
```

> 通用结尾可加：`dark horror atmosphere, embers, smoke, dramatic lighting, 16:9`
> 想要更抽象：加 `glitch effects / particle dissolve / kaleidoscope / trippy distortion`

---

## ✅ 五、完整出片流程（每期照做）

1. **配色** → 用第0步问AI拿一套本期配色，记下色值
2. **音乐** → Suno 生成 + Extend 拼到 10 分钟（纯器乐），记下曲风/BPM/段落结构
3. **缩略图** → GPT-Image 用第二节模板（填入配色 + 留标题位）
4. **生成分镜** → 用 §3.2 生成器，填入本期歌曲信息 → AI 吐出 CSV（22 个贴合本期的分镜）
5. **出图** → 存成 .csv，把 `image_prompt_en` 列逐个喂 GPT-Image 出关键帧
6. **分镜视频** → Veo3 图生视频，用 CSV 里 `motion_hint` 列做运动提示，静音
7. **剪辑** → 按 `beat_cue` 列对着音乐鼓点/Drop 卡点拼接，铺满 10 分钟
8. **统一** → 全程用同一套配色 + 死神主角，保证视觉连贯

---

## 💡 小贴士
- **一致性**：每期固定"死神长相 + 配色"，观众容易形成记忆点（系列感）
- **卡点**：MV片段在 Drop（炸点）处切换最有冲击力
- **留白**：缩略图一定留出标题文字位置，别让死神占满整屏
- **省力**：分镜 CSV 里每个镜头可做 2~3 个运动变体（推近/拉远/镜像/变速），轻松铺满 10 分钟不重复
- **分镜每期重生成**：风格锚点固定，但具体镜头用 §3.2 生成器按当期歌曲重新生成，避免每期长得一样
- **封面文字**：标题用粗描边的血迹/哥特字体，红黑或本期点缀色最抢眼
