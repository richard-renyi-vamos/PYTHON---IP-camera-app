import cv2

def show_camera():
    # Open the default camera (usually the first camera on the system)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Cannot open camera.")
        return

    print("Press 'q' to exit the camera feed.")

    while True:
        # Read a frame from the camera
        ret, frame = camera.read()

        if not ret:
            print("Error: Cannot read frame.")
            break

        # Display the frame in a window
        cv2.imshow('Live Camera Feed', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_camera()
