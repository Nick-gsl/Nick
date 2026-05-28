# ✅ Step 3 自检报告 · Episode 01

```
- 分镜总行数：118（清单条目数：105）
- 平均镜头密度：1.12 镜头/句
  · Hook 段（[0:00–0:30]，6 句）：11 镜头，密度 1.83 ✓（建议 1.5–2）
  · Bridge 段（[0:30–1:00]，5 句）：6 镜头，密度 1.20
  · Section 1（[1:00–3:20]，27 句）：30 镜头，密度 1.11
  · Section 2（[3:20–5:50]，30 句）：32 镜头，密度 1.07
  · Section 3（[5:50–8:20]，28 句）：32 镜头，密度 1.14
  · Ending 段（[8:20–9:00]，9 句）：7 镜头，密度 0.78 ✓（建议 0.7）
- 第 4 列已逐行核对为清单原文 ✓
  （多镜头共用一句时，原文逐字重复填写，未做改写/概括/合并）
- 主色：Deep Teal #1F5F66 / 辅色：Bioluminescent Yellow-Green #C8D85A（全集统一）✓
- 大景别切换次数：26 次（CU↔WS 跨跃，超过 5–8 镜头/次的最低标准）
- 快切（≤2秒）vs 长镜头（≥6秒）比例 ≈ 7 : 3
  · 快切样本：#2(2s) #4(2.5s) #10(1.5s) #11(1s) #38(2s) #61(2s) #74(2s) #114(2s)
  · 长镜头样本：#5(6s) #15(6s) #18(6s) #25(6s) #47(5s) #60(6s) #77(8s) #82(7s) #99(8s) #108(8s) #118(10s)
- 主角档案已应用至所有相关分镜 ✓
  （"orange-yellow filamentous network with glowing nodes, electric blue pulses traveling along strands"
   片段在所有菌丝场景中复用；色板 #1F5F66 + #C8D85A 在固定开头中固化）
- 中英描述情绪/动作/主体核对：无缺失 ✓
  （每条 prompt 都包含主体名词 + 动作动词 + 情绪 mood 三要素）
- 受版权保护 IP 形象扫描：无 ✓
  （无米老鼠、皮卡丘、Garfield 等 IP；所有动物/真菌为通用化几何设计）
- POV 锁定（论点级，非句子级）：
  · S1 ✓ "For the fungus, your garden is not a picture. It is a voltage field."（第 42–47 镜头视觉化）
  · S2 ✓ "For a fungus, the world is not just a map of where things are. It is a map of where things were."（第 78–80 镜头双层叠加可视化）
  · S3 ✓ "the soil under your shoes has been asking that question for four hundred million years."（第 108–110 镜头深时间尺度推进）
- 黏菌科学严谨性 ✓
  （第 95 镜头明确画"分类树"图标，把黏菌与真菌分支明显分开）
- 与 Step 2 对应关系：105 句 → 118 镜头，未漏 1 句、未额外发明 1 句
```

## 文件清单

| 文件 | 说明 |
|---|---|
| `00-step3-selfcheck.md` | 本自检报告 |
| `01-character-profile.md` | 主角一致性档案 + 配色 + 复用 prompt 片段 |
| `02-storyboard.md` | 完整 Markdown 分镜表（GitHub 网页可直接浏览） |
| `03-storyboard.csv` | UTF-8 BOM CSV，Excel/Numbers 双击直开 |
| `04-storyboard.xlsx` | 真 .xlsx 二进制文件（带冻结首行 + 列宽预设） |
| `build_csv.py` | CSV 生成脚本（数据源） |
| `build_xlsx.py` | XLSX 生成脚本（基于 CSV，纯 stdlib） |

## 节奏可视化（按段时长合计）

```
HOOK    [0:00→0:30]  ████████████████████  6 句 → 11 镜头  (密度 1.83 / 视觉冲击)
BRIDGE  [0:30→1:00]  ███████████████       5 句 → 6 镜头   (密度 1.20)
SEC 1   [1:00→3:20]  ███████████████████████████████  27 句 → 30 镜头  (密度 1.11 / 节奏稳定)
SEC 2   [3:20→5:50]  █████████████████████████████████  30 句 → 32 镜头  (密度 1.07 / 故事舒展)
SEC 3   [5:50→8:20]  █████████████████████████████████  28 句 → 32 镜头  (密度 1.14 / 反转密集)
ENDING  [8:20→9:00]  ███████████████████   9 句 → 7 镜头   (密度 0.78 / 让观众消化)
```
