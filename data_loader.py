import pandas as pd

def load_and_clean_data(file_path):
    """
    读取Excel数据并进行预处理
    1. 读取数据
    2. 删除前5行无用数据
    3. 清除全为空的列
    """
    # 读取数据
    df = pd.read_excel(file_path, header=2)
    
    # 清理前五行无用数据
    df = df.drop([0,1,2,3,4])
    df.reset_index(drop=True, inplace=True)
    
    # 删除全部为空的列
    df.dropna(axis=1, inplace=True)
    
    return df