import requests
import os


class DownloadEVImages:
    def __init__(self):
        self.download_dir = ''
        self.set_download_dir('images/')
        with open('urls.txt') as file:  # Open txt file that contains all of the urls.
            self.urls = file.read().splitlines()  # Ignore the line breaks, so they aren't included in the list.

    def download_image(self, url):
        """ Make a request to download the image with the specified url and return the result.

        Args:
            url: A string defining url of the image that is to be downloaded.

        Returns:
             response: A requests object containing the responses content and url.
        """
        response = requests.get(url)
        print('Downloaded image: {}'.format(url[48:]))
        return response

    def save_image(self, response):
        """ Saves the image with the image id within the specified download directory.

        Open a new .jpg file created using the url (image id) from the response, then with this newly
        create .jpg file write the content of the response to it. (bytes)

        Args:
            response: A requests object containing the responses content and url.
        """
        with open("{} {}".format(self.download_dir, response.url[48:]), 'wb') as image:
            image.write(response.content)
        print('Saved image: {}, saved in {}'.format(response.url[48:], self.download_dir))

    def download_random_image(self):
        """ Download and save a random single image. """
        import random
        image = self.download_image(random.choice(self.urls))
        self.save_image(image)

    def download_all_images(self):
        """ Download and save all of images. """
        for url in self.urls:
            image = self.download_image(url)
            self.save_image(image)

    def download_range_of_images(self, start, end):
        """ Download and save a range of images.

        Args:
            start: The start index of the urls slice. Used to indicate where the user wishes their range to start.

            end: The end index of the urls slice. Used to indicate where the user wishes their range to end.
        """
        for url in self.urls[start:end]:
            image = self.download_image(url)
            self.save_image(image)

    def set_download_dir(self, path):
        """ Sets the location where the images shall be downloaded to.

        First checks to see if the location exists before setting the download direction.
        If the location doesn't already exists then create the directory.

        Args:
            path: A string defining the desired path for the download directory.
        """
        if not os.path.exists(path):
            os.mkdir(path)
        self.download_dir = path


def present_menu():
    """ Present the menu to user so they can make their choice and have it acted upon. """
    print('1. Download a random image')
    print('2. Download a range of images')
    print('3. Download all Earth View images')
    choice = int(input('Please choose one of the above options: '))
    if choice == 1:
        earth_view.download_random_image()
    elif choice == 2:
        start = int(input('Please define a starting position - smallest value 0: '))
        end = int(input('Please define an end position - largest value 1523: '))
        if start < end:
            if start >= 0 and end <= 1523:
                earth_view.download_range_of_images(start, end)
            else:
                print('start or end position is out of bounds!')
        else:
            print('start must be smaller than the end position')
    elif choice == 3:
        earth_view.download_all_images()
    else:
        present_menu()  # User has provided an incorrect choice value so present the menu to the user again.

if __name__ == '__main__':
    earth_view = DownloadEVImages()
    present_menu()

