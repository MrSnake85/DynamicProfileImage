from datetime import date


class GuildMember:
    def __init__(self,
                 user_id,
                 name,
                 level=1,
                 points=0,
                 last_activity=None,
                 msg_counter=0,
                 vc_time=0,
                 birthday=None,
                 battle_tag=None,
                 steam_code=None,
                 weekly_update=True):
        if last_activity is None:
            last_activity = date.today()

        # database values
        self.user_id = user_id                                  # discord user id
        self.name = name                                        # discord user name
        self.level = level                                      # current activity level
        self.points = points                                    # the current amount of points
        self.last_activity = last_activity                      # last activity date (voice or text)
        self.msg_counter = msg_counter                          # counter for messages written
        self.vc_time = vc_time                                  # counter for time in voice chat
        self.birthday = birthday                                # birthdate of the guild member
        self.battle_tag = battle_tag                            # battle net tag of this guild member
        self.steam_code = steam_code                            # steam name of this user
        self.weekly_update = weekly_update                      # indicator if the guild member has weekly updates activated
