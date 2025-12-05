from os import write


class Story():
    def __init__(self):
        self.user_input: float
        self.input_unit: str
        self.result: float
        self.output_unit: str

    def save_data(self, user_input, input_unit, result, output_unit):
        try:
            with open("story.txt", "a") as story_file:
                story_file.write(f"{user_input} {input_unit} = {result} {output_unit}\n")
        except:
            with open("story.txt", "w") as story_file:
                story_file.write(f"{user_input} {input_unit} = {result} {output_unit}\n")

    def read_data(self):
        with open("story.txt", "r") as story_file:
            story_list = story_file.readlines()
            for i in range(len(story_list)):
                print(f"{[i + 1]}: {story_list[i]}\n")

    def delete_story(self):
        try:
            with open("story.txt", "w") as story_file:
                story_file.write("")
        except:
            print("Файла с историей еще нет")
