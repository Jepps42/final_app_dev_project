import app

anime_dict = {


}



def favorite_animes(animes):
    if animes == "Drama":
        anime_dict["Anime1"] = "Hunter X Hunter"
        anime_dict["Anime2"] = "Demon Slayer" 
        return anime_dict
    elif animes == "Action":
        anime_dict["Anime1"] = "Kuroko Basketball"
        anime_dict["Anime2"] = "Haikyuu"
        return anime_dict
    elif animes == "Slice of Life":
        anime_dict["Anime1"] = "The Disastrous Life of Saiki K"
        anime_dict["Anime2"] = "Haven't You Heard? I'm Sakamoto"
        return anime_dict
    else:
        anime_dict["Anime1"] = "Error! "
        anime_dict["Anime2"] = "You have not chosen the correct genre we offered"
        return anime_dict