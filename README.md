# Posture Detection using OpenCV and MediaPipe

This project implements a real-time posture detection system using OpenCV and MediaPipe. The system accurately detects and classifies human postures from live video feeds, offering potential applications in ergonomic assessment, fitness tracking, physical therapy, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Applications](#applications)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Real-Time Detection**: Processes live video streams to identify and classify human postures in real time.
- **Key Point Detection**: Leverages MediaPipe's pose estimation to accurately detect key body landmarks.
- **Cross-Platform Compatibility**: Compatible with various operating systems, including Windows, macOS, and Linux.
- **Customizable**: Easily extend or modify the detection algorithms to suit different posture-related use cases.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/pratham-asthana/posture-detection.git
    cd posture-detection
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script to start the posture detection system:

    ```bash
    python main.py
    ```

2. The system will begin processing the webcam feed, detecting and classifying postures in real time.

## Customization

You can modify the posture detection logic in `main.py` to adapt the system to different use cases or add more complex posture classifications. For example, you might add additional conditions or use more advanced machine learning models for classification.

## Applications

- **Workplace Ergonomics**: Monitor and improve posture in office environments.
- **Fitness Tracking**: Analyze and correct posture during exercises.
- **Physical Therapy**: Assist in rehabilitation by tracking patient movements.

## Contributing

Contributions are welcome! If you have ideas to improve the project or want to fix a bug, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
