import pandas as pd

def calculate_scores(df):
    """计算每个学生的总分和平均分"""
    score_cols = df.iloc[:, 4:20]
    df['总分'] = score_cols.sum(axis=1)
    df['平均分'] = score_cols.mean(axis=1).round(2)
    return df

def get_subject_max_info(df):
    """获取各科最高分和对应姓名"""
    subjects = df.iloc[:, 4:20].columns
    
    def get_max(col):
        return df[col].max()
    
    def get_top_names(col):
        max_val = df[col].max()
        names = df[df[col]==max_val]['姓名'].tolist()
        return ', '.join(names)
    
    max_list = [get_max(c) for c in subjects]
    name_list = [get_top_names(c) for c in subjects]
    
    return pd.DataFrame({
        '科目': subjects,
        '最高分': max_list,
        '姓名': name_list
    })

def create_grade_level_df(df):
    """
    对所有科目进行分箱
    英语+日语 → 合并为外语
    其他科目单独分箱
    """
    bins = [0, 60, 70, 80, 90, 101]
    labels = ["不及格", "及格", "中等", "良好", "优秀"]
    
    df_level = pd.DataFrame()
    df_level["姓名"] = df["姓名"]
    
    # 外语整合
    df_level["外语"] = (df["2大学日语(A)Ⅲ"] + df["2大学英语(A)Ⅲ"])
    df_level["外语_等级"] = pd.cut(df_level["外语"], bins=bins, labels=labels,right=False)
    
    # 其他科目分箱
    subjects = df.iloc[:, 4:20].columns
    for col in subjects:
        if "日语" not in col and "英语" not in col:
            df_level[col + '_等级'] = pd.cut(df[col], bins=bins, labels=labels,right=False)
    
    return df_level

def total_grade_count(df_level):
    """统计所有科目等级总次数"""
    level_cols = [col for col in df_level.columns if '_等级' in col]
    total_count = pd.Series(dtype='int64')
    
    for col in level_cols:
        cnt = df_level[col].value_counts()
        total_count = total_count.add(cnt, fill_value=0)
    
    total_count = total_count.astype(int)
    order = ['不及格', '及格', '中等', '良好', '优秀']
    return total_count.reindex(order)