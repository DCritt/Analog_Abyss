import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music = {}
        self.channels = {}

    def init_sounds(self, root_dir):
        audio_path = root_dir / "assets" / "audio"

        music_path = audio_path / "music"

        oleum_path = music_path / "oleum.ogg"
        self.load_music("oleum", str(oleum_path))

        ambient_path = music_path / "ambient_noise.ogg"
        self.load_music("ambient", str(ambient_path))

        sound_effects_path = audio_path / "sound_effects"

        low_step_path = sound_effects_path / "low_footstep.wav"
        med_step_path = sound_effects_path / "med_footstep.wav"
        high_step_path = sound_effects_path / "high_footstep.wav"
        self.load_sound("low_step", str(low_step_path))
        self.load_sound("med_step", str(med_step_path))
        self.load_sound("high_step", str(high_step_path))

    def load_sound(self, name, path):
        self.sounds[name] = pygame.mixer.Sound(path)

    def load_music(self, name, path):
        self.music[name] = path

    def play_sound(self, name, volume=1.0, loops=0):
        sound = self.sounds[name]
        sound.set_volume(volume)
        return sound.play(loops=loops)

    def play_sound_on_channel(self, name, channel_id, volume=1.0, loops=0):
        if channel_id not in self.channels:
            self.channels[channel_id] = pygame.mixer.Channel(channel_id)
        sound = self.sounds[name]
        sound.set_volume(volume)
        self.channels[channel_id].play(sound, loops=loops)

    def play_music(self, name, volume=1.0, loops=-1):
        if name is None:
            pygame.mixer.music.stop()
            return
        path = self.music[name]
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops)