# Ball-Trajectory-Prediction

A computer vision application that tracks a basketball in a video, predicts its trajectory using polynomial curve fitting, and determines whether the shot will result in a basket or not.

## 🏀 Features

- **Real-time Ball Tracking**: Uses HSV color-based detection to track basketball movement
- **Trajectory Prediction**: Implements polynomial curve fitting (2nd degree) to predict ball path
- **Basket Prediction**: Determines if the shot will land in the basket area
- **Interactive Visualization**: Displays tracking points, trajectory line, and prediction result
- **Multiple View Outputs**: Shows processed images with contours, predictions, and results

## 📋 Requirements

- Python 3.7+
- OpenCV
- NumPy
- cvzone library

## 🔧 Installation

1. Clone this repository:
```bash
git clone https://github.com/nowherewalrus/Ball-Trajectory-Prediction.git
cd Track_Pred
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Place your basketball video file in the project directory (rename it to `vid (5).mp4` or update the filename in the code)

2. Run the script:
```bash
python Track_Pred.py
```

3. Controls:
   - **ESC**: Exit the application
   - **S**: Restart tracking (clear previous data and start fresh)

## 📊 How It Works

1. **Color Detection**: The program uses HSV color filtering to detect the orange basketball
2. **Contour Tracking**: Identifies the ball's position frame by frame
3. **Curve Fitting**: Uses polynomial regression on collected positions to predict trajectory
4. **Basket Prediction**: Calculates where the ball will land relative to the basket position
5. **Visualization**: Displays tracking points, predicted path, and final prediction result

## ⚙️ Configuration

### HSV Values
Adjust these values in the code to match your basketball color:
```python
hsvVals = {'hmin': 8, 'smin': 124, 'vmin': 13, 'hmax': 24, 'smax': 255, 'vmax': 255}
```

### Basket Position
The basket line is fixed at y-coordinate 593. Modify this line in the code:
```python
c = c - 593  # This is the basket height
```

### Prediction Threshold
The basket area is defined between x-coordinates 300-430:
```python
prediction = 300 < x < 430
```

## 🎯 Performance Notes

- The program needs at least 10 frames of ball tracking for initial prediction
- Works best with consistent lighting and clear ball visibility
- May require HSV value adjustments for different lighting conditions
- Performance depends on video quality and ball contrast

## 📁 File Structure

```
basketball-predictor/
├── Track_Pred.py  # Main application code
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── vid (5).mp4            # Sample video (not included)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- [cvzone](https://github.com/cvzone/cvzone) for computer vision utilities
- OpenCV community for excellent computer vision tools
- Contributors and testers

## 🐛 Troubleshooting

1. **No ball detected**: Adjust HSV values in the code
2. **Poor tracking**: Ensure good lighting and contrast
3. **Incorrect predictions**: Check basket position coordinates
4. **Import errors**: Verify all packages are installed correctly

---

**Note**: Replace `vid (5).mp4` with your video filename or modify the code accordingly.
