This tool is used to **create image datasets** from **videos**.

**Instructions to setup:
**1. Install python 3.X with pip added to path.
2. Run "pip install -r requirements.txt" to install all the required dependencies for this project.
3. Run 'index.py' file to use this tool.

**How to use this tool:
**1. Place the videos in the 'videos' folder in root directory.
2. Open index.py
3. Since all of the GI videos are in .avi extension, no need to enter the extension. For example, if the video name is 'patient_1.avi', type 'patient_1' and press enter. In case, if you would like to use a video format other that .avi format, please opent the index.py file and change the '.avi' to your desired format in line 34.
4. It should take you to the page where you can select the landmarks from the video.
5. You can play/pause the video and also you can use slide to move to anypoint of the video.
6. If you want to mark the landmark as the current frame that you are seeing, click of the '/' next to respetive landmark in right side panel. There will be 9 landmarks plus no_mans_land option. You can navigate through them using the arrow at top of right side panel.
7. Once you click the '/', it'll ask you confirmation message. If you click 'yes', it'll save the 10 frames (-5 to +5) of current frame in the 'dataset' folder.
8. Once you are done marking all the landmarks, you can click on proceed to finish.

If you face any issues or have any queries, drop a mail to me at **gvsunilkumar2001@gmail.com**
