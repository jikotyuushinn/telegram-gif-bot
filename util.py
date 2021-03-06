from functools import wraps
import moviepy.editor as mp
from telegram import ChatAction

def send_action(action):
    """
    Sends `action` while processing func command.
    :param action:
    :return:
    """

    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(update, context,  *args, **kwargs)
        return command_func

    return decorator

typing = send_action(ChatAction.TYPING)
uploading_video = send_action(ChatAction.UPLOAD_VIDEO)

def mp4_to_gif(file_name, new_file_name):
    clip = mp.VideoFileClip(file_name, audio=False)
    clip.write_gif(new_file_name)
