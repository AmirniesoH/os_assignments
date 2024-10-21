# Standalone corrective
 
## پکیج های مورد نیاز و نسخه مربوطه:

```bash
matplotlib == 3.4.3
opencv-python-headless == 4.6.0.66
opencv-contrib-python-headless == 4.6.0.66
absl-py == 1.2.0
attrs == 22.1.0
protobuf == 3.20.2
mediapipe == 0.8.9
scipy == 1.8.0
natsort == 8.1.0
```

### نکات قابل توجه:

<ul>
    <li>
    آدرس دهی ها در ابتدای فایل app.py با توجه به محل قرار نصب شده پکیح ها آپدیت شوند.
    </li>
    <li>
    دو نکته حائز اهمیت است:
        <ul>
            <li>
            فایل drawing_utils.py باید  جایگزین شود
            </li>
            <li>
            مدل های tflite باید در مسیر مربوطه کپی شوند. (مسیر آنها در فایل داکر مشخص است)
            </li>
        </ul>
    </li>
    
</ul>



