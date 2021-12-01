import matplotlib.pyplot as plt

def plot_exponent_histogram(x_axis_values, y_axis_fp32_values, y_axis_fp64_values, plot_name):
    x_axis_label_position = list(range(len(x_axis_values)))
    plt.clf()
    plt.xticks(x_axis_label_position, x_axis_values)

    x_axis_label_position[:] = [number - 0.2 for number in x_axis_label_position]
    plt.bar(x_axis_label_position, y_axis_fp32_values, 0.4, label="LULESH FP32")

    x_axis_label_position[:] = [number + 0.4 for number in x_axis_label_position]
    plt.bar(x_axis_label_position, y_axis_fp64_values, 0.4, label="LULESH FP64")

    plt.legend(prop={"size":12})
    plt.xlabel('Exponent Range', fontsize=14)
    plt.ylabel('Counts', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.savefig(plot_name)


if __name__ == '__main__':
    keys = ["<5%", "5%-95%", ">95%"]
    temp_dict = {'fp32': {'low': 4290706, 'regular': 23952416, 'high': 4116},
                    'fp64': {'low': 3613970, 'regular': 24634345, 'high': 0}}

    plot_name = 'temp'

    plot_exponent_histogram(keys,
                            list(temp_dict['fp32'].values()),
                            list(temp_dict['fp64'].values()),
                            plot_name + '.png')