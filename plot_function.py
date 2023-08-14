def print_barplot(data, x, hue=None, x_order=None, hue_order=None, title=None, y_label=None):
    sns.countplot(x=x, hue=hue, data=data, dodge=True, order=x_order, hue_order=hue_order)
    
    plt.title(title)
    plt.xlabel("{}".format(x))
    plt.ylabel(y_label)

    # 범례 추가
    plt.legend()

    # 그래프 보여주기
    plt.show()