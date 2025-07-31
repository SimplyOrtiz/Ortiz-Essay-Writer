# Ortiz's Essay Writer (OEW)

### What is it?

**Ortiz's Essay Writer** (OEW) is a small, user-friendly Python application designed to **automate repetitive typing tasks**. Simply input your desired text, and OEW will type it out for you, saving you time and effort, especially for long-form entries.

### Features

  * **Intuitive Graphical User Interface (GUI):** Easy-to-use window for seamless text input and settings management.
  * **Customizable Typing Speed:** Adjust the typing delay to suit your system's performance or your preference.
  * **Simple Activation:** Start typing with a quick key press after preparing your text.

-----

### Download & Installation (Recommended for most users)

The easiest way to get OEW is to download the pre-built executable (`.exe`) file directly from the GitHub Releases page. No Python installation or additional libraries are required\!

1.  **Go to the Releases Page:** Visit [https://github.com/SimplyOrtiz/Ortiz-Essay-Writer/releases/tag/Release](https://github.com/SimplyOrtiz/Ortiz-Essay-Writer/releases/tag/Release)
2.  **Download the Executable:** Look for the `OrtizEssayWriter.exe` (or similarly named) file under the "Assets" section of the latest release. Click to download it.
3.  **Run the Application:** Once downloaded, simply double-click the `.exe` file to launch OEW.

-----

### How to Use

1.  **Prepare the Text:** Launch the OEW application. In the main window, paste or type the text you want to be automatically typed into the large text area.

2.  **Adjust Typing Speed (Optional):**

      * If you want to control the typing speed (e.g., for slower computers or specific scenarios), navigate to the top menu bar.
      * Click on **"File"** and then select **"Speed"**.
      * A new window will appear. Enter your desired delay time (in seconds) in the input box.
      * Enter `0` for no delay (fastest typing), or a higher decimal value (e.g., `0.01`, `0.1`, `0.5`) to slow down typing.
      * Click "Save and Go back" to apply the setting.

3.  **Start Typing:**

      * Once your text is ready in OEW's text area, click the **"Write"** button located below the text box.
      * The OEW status will change to "Press '1' to start writing the text...".
      * Now, quickly click on the text box or document where you want the text to be written (e.g., a web browser text field, a word processor).
      * Finally, press the **`1`** key on your keyboard to trigger the automatic typing process. OEW will indicate "Writing..." and then "Finished" when complete.

-----

### Building from Source (For Python Developers)

If you prefer to run OEW directly from the Python source code or want to modify it, follow these steps:

1.  **Prerequisites:** You'll need Python installed on your machine.
2.  **Install Dependencies:** OEW requires the `keyboard` library. Install it using pip:
    ```bash
    pip install keyboard
    ```
3.  **Run the Script:** Download or clone the repository, then run the `essay_writer.py` file:
    ```bash
    python essay_writer.py
    ```

-----

> [\!NOTE]
> If you experience lag or skipped characters during typing, especially on lower-performance computers, adjust the typing delay. A higher delay value will make the typing process smoother. You can set this in the "Speed" settings window.

-----