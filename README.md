# Ortiz's Essay Writer (OEM)

### What is it?
**Ortiz's Essay Writer** (OEM) is a small Python program that automates typing by writing all the text from the `essaytext.txt` file. It is designed to help users automate repetitive typing tasks, especially useful for long-form text entries.

### How to Install
To install OEM, you’ll need Python installed on your machine, along with two libraries: `time` and `keyboard`. You can install these libraries using pip:

```bash
$ pip install keyboard
```

Alternatively, you can install all required libraries using the provided `requirements.txt` file:

```bash
$ pip install -r requirements.txt
```

Make sure the command prompt is set to the directory where the `requirements.txt` file is located.

### How to Use

1. **Prepare the text**: Place the text you want to be automatically typed inside the `essaytext.txt` file.
   
2. **Adjust typing delay (optional)**: If your computer is slow or you want to control the typing speed, you can set a delay between each character. When you run the program, it will prompt you to input a delay time (in seconds). Enter `0` for no delay, or a higher value to slow down typing.

3. **Run the program**: Open the command prompt in the directory where `essayWriter.py` is located and run the following command:

```bash
$ py essayWriter.py
```

4. **Start typing**: Once the script starts, click on the text box where you want the text to be written (e.g., a document or browser text field). Then, press `1` on your keyboard to trigger the typing process.

5. **Warning about performance**: If your computer has lower performance, typing might lag when pressing `1`. You can adjust the delay by entering a higher value when prompted or modifying the `DelayTime` parameter in the code.

### Customization

- **Change trigger key**: By default, the script starts typing when you press `1`. You can change this trigger key to any other key by modifying the `keyboard.wait("1")` line in the code.
  
- **Delay Time**: If you experience lag, you can change the `DelayTime` inside the script or when prompted, making the typing process smoother for slower machines.