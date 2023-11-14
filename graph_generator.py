from utils import generate_and_save_graphs

def main():
    v_range = range(4, 265)
    percentage = [0.125, 0.25, 0.5, 0.75]
    student_number = 104142
    file = 'graphs.pickle'

    generate_and_save_graphs(v_range, percentage, student_number, file)

if __name__ == "__main__":
    main()