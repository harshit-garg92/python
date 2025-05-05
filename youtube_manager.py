import json


def load_data():
    try:
        with open('you.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
        

def save_data_help(videos):
    with open('you.txt','w') as file:
        json.dump(videos, file)


def list_all_vid(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.{video['name']}, duration :{video['time']} ")
    print("\n")
    print("*"*70)



def add_video(videos):
    name = input("enter name:")
    time = input("enter time:")
    videos.append({'name': name,'time': time})
    save_data_help(videos)




def update_video(videos):
    list_all_vid(videos)
    i = int(input("enter the no"))
    if 1 <= i <= len(videos):
        name = input("enter the new name") 
        time = input("enter the new time")
        videos[i-1]= {'name':name,'time':time} 
        save_data_help(videos)
    else:
        print("invalid index")





def delete_video(videos):
    list_all_vid(videos)
    i = int(input("enter no"))

    if 1 <= i <= len(videos):
        del videos[i-1]
        save_data_help(videos)
    else:
        print("invalid index")





def main():
    videos = load_data()
    while True:
        print("\n youtube manage")
        print("1.list all video")
        print("2.add vid")
        print("3.update vid details")
        print("4.delete a video")
        print("5.exit")
        choice=input("enetr choice: ")
        #print(videos)

        match choice:
            case '1':
                list_all_vid(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4' :
                delete_video(videos)
            case '5' :
                break
            case _  :
                print("invalid choice")            


if __name__ == "__main__" :
    main()









