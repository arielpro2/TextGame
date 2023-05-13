from glob import glob
class LevelLoader:
    def __init__(self, map_folder):
        self.map_folder = map_folder
        self.maps=[]
        for text_file in glob(map_folder+'/*'):
            map_id = text_file[3::]
            with open(text_file, 'r') as f:
                self.maps.append([line.replace('\n', '') for line in f.readlines()])

    def load_map(self, map_id: int):
        for line in self.maps[map_id]:
            print(line)

