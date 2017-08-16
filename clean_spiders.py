import os


def clean():
    for file in os.listdir("projects/newspaper/spiders"):
        file = "projects/newspaper/spiders/" + file
        if os.path.isdir(file):
            os.popen("rm -rf " + file)
            os.remove(file + ".json")


if __name__ == '__main__':
    clean()
