import matplotlib.pyplot as plt
import pandas as pd

def plot_all_subjects(df_level):
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    order = ['优秀', '良好', '中等', '及格', '不及格']
    colors = ['blue', 'blue', 'blue', 'blue', 'red']
    level_cols = [col for col in df_level.columns if '_等级' in col]

    # 自动分成 2 张图
    mid = len(level_cols) // 2
    part1 = level_cols[:mid]
    part2 = level_cols[mid:]

    # --------- 第一张图 ---------
    rows1 = (len(part1) + 1) // 2
    fig1, axes1 = plt.subplots(rows1, 2, figsize=(16, 5 * rows1))
    axes1 = axes1.flatten()

    for i, col in enumerate(part1):
        cnt = df_level[col].value_counts().reindex(order)
        ax = axes1[i]
        cnt.plot(kind='bar', color=colors, ax=ax)
        title = col.replace('_等级', '')
        ax.set_title(title, fontsize=14)
        ax.set_ylabel('人数')
        ax.set_xticklabels(order, rotation=0)
        
        for j, v in enumerate(cnt):
            if pd.notna(v):
                ax.text(j, v + 0.2, str(int(v)), ha='center')

    for j in range(i + 1, len(axes1)):
        axes1[j].axis('off')

    fig1.suptitle('成绩等级分布 1', fontsize=20)
    plt.tight_layout()

    # --------- 第二张图 ---------
    rows2 = (len(part2) + 1) // 2
    fig2, axes2 = plt.subplots(rows2, 2, figsize=(16, 5 * rows2))
    axes2 = axes2.flatten()

    for i, col in enumerate(part2):
        cnt = df_level[col].value_counts().reindex(order)
        ax = axes2[i]
        cnt.plot(kind='bar', color=colors, ax=ax)
        title = col.replace('_等级', '')
        ax.set_title(title, fontsize=14)
        ax.set_ylabel('人数')
        ax.set_xticklabels(order, rotation=0)
        
        for j, v in enumerate(cnt):
            if pd.notna(v):
                ax.text(j, v + 0.2, str(int(v)), ha='center')

    for j in range(i + 1, len(axes2)):
        axes2[j].axis('off')

    fig2.suptitle('成绩等级分布 2', fontsize=20)
    plt.tight_layout()

    plt.show()