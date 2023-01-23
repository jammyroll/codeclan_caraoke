class Room:
    def __init__(self,name,till):
        self.name = name
        self.singers = []
        self.song_list = []
        self.till = till

    def add_guest(self,guest):
        if len(self.singers) >= 4:
                return "Sorry the room is full, try another"
        else:
            guest.wallet -= 5
            self.till += 5
            self.singers.append(guest)


    def remove_guest(self,guest):
        self.singers.remove(guest)

    def add_song_to_room(self,song):
        self.song_list.append(song)
        for people in self.singers:
            if people.top_song == song.song_name:
                    return( f"{people.name} yells Woo")

        else:
            return 'I want my fav song'

