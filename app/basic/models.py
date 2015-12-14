import os
import random
import string

from flask import current_app, request


class UploadManager(object):
    @staticmethod
    def upload_avatar(image):
        if image.content_type:
            filename = generate_random_string(20) + \
                       os.path.splitext(image.filename)[1]
            image.save(os.path.join(current_app.config['AVATAR_UPLOAD_FOLDER'],
                                    filename))
            print("Image uploaded: {}".format(filename))
            return filename

    @staticmethod
    def upload_tour_images():
        buffer = []

        for image in request.files.getlist('images'):
            if image.content_type:
                filename = generate_random_string(20) + \
                           os.path.splitext(image.filename)[1]

                image.save(os.path.join(
                        current_app.config['TOUR_IMAGES_UPLOAD_FOLDER'],
                        filename)
                )

                buffer.append(filename)

        return ";".join(buffer)


def generate_random_string(length):
    return "".join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(length))
