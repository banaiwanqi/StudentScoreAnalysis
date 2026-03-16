from data_loader import load_and_clean_data
from analyzer import calculate_scores, get_subject_max_info, create_grade_level_df, total_grade_count
from visualizer import plot_all_subjects

# 1. 读取并清洗数据
file_path = r'C:/Users/ASUS/Project/Exercise/Exercises_Data/1.2025-2026学年第一学期学业成绩表.xls'
df = load_and_clean_data(file_path)

# 2. 计算总分、平均分
df = calculate_scores(df)

# 3. 输出平均分排名
print("平均分排名：")
print(df[['姓名', '平均分']].sort_values(by='平均分', ascending=False))

# 4. 各科最高分
max_df = get_subject_max_info(df)
print("\n各科最高分：")
print(max_df)

# 5. 分箱等级
df_level = create_grade_level_df(df)

# 6. 统计总次数
total_count = total_grade_count(df_level)
print("\n所有科目等级总次数：")
print(total_count)

# 7. 可视化所有科目
plot_all_subjects(df_level)