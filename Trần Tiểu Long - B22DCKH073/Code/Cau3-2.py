import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

def plot_radar_chart(data, player1, player2, attributes):
    # Lấy dữ liệu của hai cầu thủ
    p1_data = data[data['Player Name'] == player1].iloc[0][attributes].values.astype(float)
    p2_data = data[data['Player Name'] == player2].iloc[0][attributes].values.astype(float)

    # Số lượng thuộc tính
    num_vars = len(attributes)

    # Tạo các góc cho biểu đồ radar
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Khép kín biểu đồ
    p1_data = np.concatenate((p1_data, [p1_data[0]]))
    p2_data = np.concatenate((p2_data, [p2_data[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # Vẽ biểu đồ radar cho từng cầu thủ
    ax.plot(angles, p1_data, color='blue', linewidth = 2, linestyle='solid', label=player1)
    ax.fill(angles, p1_data, color='blue', alpha=0.25)

    ax.plot(angles, p2_data, color='red', linewidth = 2, linestyle='solid', label=player2)
    ax.fill(angles, p2_data, color='red', alpha=0.25)

    # Thêm các thuộc tính trên các trục
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)

    # Thêm tiêu đề và chú thích
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.title(f'Comparison between {player1} and {player2}')

    plt.show()

def main():
    # Khởi tạo parser để lấy thông số đầu vào
    parser = argparse.ArgumentParser(description='Compare two players using radar chart.')
    parser.add_argument('--p1', type=str, required=True, help='Player 1 name')
    parser.add_argument('--p2', type=str, required=True, help='Player 2 name')
    parser.add_argument('--Attribute', type=str, required=True, help='List of attributes to compare, separated by commas')

    args = parser.parse_args()\
    
    # Đọc dữ liệu từ file CSV   
    data = pd.read_csv('results.csv')
    
    player1 = args.p1
    player2 = args.p2
    attributes = args.Attribute.split(',')


    for attr in attributes:
        data[attr] = pd.to_numeric(data[attr], errors='coerce')

    # Vẽ biểu đồ radar
    plot_radar_chart(data, player1, player2, attributes)

if __name__ == "__main__":
    main()

# python 3.py --p1 "Aaron Cresswell" --p2 "Aaron Wan-Bissaka" --Attribute "Age,Matches Played,Starts,Minutes,Non-Penalty Goals,Penalties Made,Assists,Yellow Cards,Red Cards"