import tkinter as tk


# Function to count words in text
def word_counter(text):
    if not text.strip():
        return 0
    words = text.split()
    return len(words)


# Function to count words and update result label
def count_words():
    input_text = text_entry.get("1.0", "end-1c")
    word_count = word_counter(input_text)
    result_label.config(text=f"Word count: {word_count}")


# Function to clear text and reset word count
def clear_text():
    text_entry.delete("1.0", "end")
    result_label.config(text="Word count: 0")


# Function to change theme based on selection
def change_theme(selected_theme):
    theme_colors = {
        "Default": {"bg": "#f0f0f0", "title_bg": "#4CAF50", "title_fg": "#FFFFFF", "label_bg": "#f0f0f0",
                    "label_fg": "#333333", "entry_bg": "#FFFFFF", "button_fg": "#FFFFFF", "button_bg1": "#4CAF50",
                    "button_bg2": "#03A9F4", "count_fg": "#333333"},
        "Dark": {"bg": "#333333", "title_bg": "#2c3e50", "title_fg": "#FFFFFF", "label_bg": "#333333",
                 "label_fg": "#CCCCCC", "entry_bg": "#2c3e50", "button_fg": "#FFFFFF", "button_bg1": "#27AE60",
                 "button_bg2": "#3498db", "count_fg": "#FFFFFF"},
    }

    # Apply theme colors to different elements
    window.configure(bg=theme_colors[selected_theme]["bg"])
    title_label.config(bg=theme_colors[selected_theme]["title_bg"], fg=theme_colors[selected_theme]["title_fg"])
    label.config(bg=theme_colors[selected_theme]["label_bg"], fg=theme_colors[selected_theme]["label_fg"])
    text_entry.config(bg=theme_colors[selected_theme]["entry_bg"])
    count_button.config(bg=theme_colors[selected_theme]["button_bg1"], fg=theme_colors[selected_theme]["button_fg"])
    clear_button.config(bg=theme_colors[selected_theme]["button_bg2"], fg=theme_colors[selected_theme]["button_fg"])

    # Update result_label's foreground color for both themes
    result_label.config(fg=theme_colors[selected_theme]["count_fg"])

    # Adjust result_label's background color for Dark mode
    if selected_theme == "Dark":
        result_label.config(bg="#333333")
    else:
        result_label.config(bg="#f0f0f0")


# Create main window
window = tk.Tk()
window.title("Word Counter")
window.geometry("600x500")

# Set initial theme
selected_theme = tk.StringVar(window)
selected_theme.set("Default")

# Theme selection dropdown
themes = ["Default", "Dark"]
theme_menu = tk.OptionMenu(window, selected_theme, *themes, command=lambda _: change_theme(selected_theme.get()))
theme_menu.pack(side="bottom", padx=10, pady=10, anchor="se")

# UI elements
title_label = tk.Label(window, text="Word Counter", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="#FFFFFF", padx=10,
                       pady=10)
title_label.pack(fill="x")

label = tk.Label(window, text="Enter a sentence or paragraph:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12))
label.pack(pady=10)

text_entry = tk.Text(window, height=10, width=50, bg="#FFFFFF", font=("Helvetica", 11), padx=10, pady=10, bd=2,
                     relief="solid")
text_entry.pack(pady=10)

count_button = tk.Button(window, text="Count Words", command=count_words, bg="#4CAF50", fg="#FFFFFF", padx=8, pady=3)
count_button.pack(pady=10)

clear_button = tk.Button(window, text="Clear Text", command=clear_text, bg="#03A9F4", fg="#FFFFFF", padx=10, pady=5)
clear_button.pack(pady=10)

result_label = tk.Label(window, text="Word count: 0", font=("Helvetica", 14), bg="#f0f0f0", fg="#333333")
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
