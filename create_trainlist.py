import os, argparse


def main(args):
    data_dir = args.data_dir
    text_dest_dir = args.text_dest_dir


    data_list = os.listdir(data_dir)
    data_list.sort(key= lambda a:(int(a.split('_')[2]), a.split('_')[3]))
    data_len = len(data_list)
    with open(text_dest_dir, 'a') as text_file:

        for data_ind in range(data_len//2):
            if int(data_list[2 * data_ind].split('_')[2]) != int(data_list[2 * data_ind + 1].split('_')[2]):
                print(data_list[2 * data_ind], '!=', data_list[2 * data_ind + 1])   
                break
            else:
                text_file.write('istanbul/' + data_list[2 * data_ind] + ' ' + 'istanbul/' + data_list[2 * data_ind + 1] + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monodepth dataset text creation.')

    parser.add_argument('--data_dir',          type=str,   help='type of encoder, vgg or resnet50', default='vgg')
    parser.add_argument('--text_dest_dir',       type=str,   help='path to the image', required=True)

    args = parser.parse_args()
    main(args)
