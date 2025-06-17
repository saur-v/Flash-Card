# 🇫🇷 French Language Learning Flashcards

A beautiful and interactive flashcard application built with Python's Tkinter library to help you learn French vocabulary effectively. The app features automatic card flipping, progress tracking, and a smart learning system that focuses on words you haven't mastered yet.

## ✨ Features

- **Interactive Flashcards**: Cards automatically flip from French to English after 3 seconds
- **Progress Tracking**: Words you know are removed from future study sessions
- **Smart Learning System**: Focus on words you haven't learned yet with the `to_learn.csv` system
- **Beautiful UI**: Clean, card-based interface with custom images and colors
- **Persistent Progress**: Your learning progress is saved between sessions
- **100 Common French Words**: Pre-loaded with essential French vocabulary

## 🎮 How to Use

1. **Start the Application**: Run `python main.py`
2. **Study Mode**: 
   - French word appears on the front of the card
   - Wait 3 seconds or click a button to see the English translation
3. **Mark Your Progress**:
   - ✅ **Green Button (Right)**: Click if you knew the word - it will be removed from future sessions
   - ❌ **Red Button (Wrong)**: Click if you didn't know the word - it will appear again later
4. **Continue Learning**: The app will cycle through words you haven't mastered

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x
- tkinter (usually comes with Python)
- pandas library

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/french-flashcards.git
   cd french-flashcards
   ```

2. **Install Required Dependencies**:
   ```bash
   pip install pandas
   ```

3. **Set Up Project Structure**:
   ```
   french-flashcards/
   │
   ├── main.py                 # Main application file
   ├── data/
   │   ├── french_words.csv    # Original vocabulary dataset
   │   └── to_learn.csv        # Words still being learned (auto-generated)
   └── images/
       ├── card_front.png      # Front of flashcard image
       ├── card_back.png       # Back of flashcard image
       ├── right.png           # "Known" button icon
       └── wrong.png           # "Unknown" button icon
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
french-flashcards/
│
├── main.py                    # Main application logic
├── data/
│   ├── french_words.csv       # Complete French-English vocabulary list
│   └── to_learn.csv          # Filtered list of words to study
├── images/
│   ├── card_front.png        # Flashcard front design
│   ├── card_back.png         # Flashcard back design  
│   ├── right.png             # Success/known button icon
│   └── wrong.png             # Try again/unknown button icon
└── README.md                 # This file
```

## 🔧 How It Works

### Smart Learning Algorithm
1. **First Run**: Loads all words from `french_words.csv`
2. **Subsequent Runs**: Loads only unlearned words from `to_learn.csv`
3. **Progress Tracking**: When you mark a word as "known", it's removed from `to_learn.csv`
4. **Focused Learning**: You only study words you haven't mastered yet

### Card Mechanics
- **Auto-Flip**: Cards automatically show the English translation after 3 seconds
- **Manual Control**: Click buttons to move to the next card immediately
- **Visual Feedback**: Card changes color and design when flipped

## 📊 Vocabulary Dataset

The app includes 100 common French words covering:
- Basic nouns (family, body parts, places)
- Common verbs (actions, movement)
- Adjectives (descriptions, emotions)  
- Function words (pronouns, conjunctions)
- Time expressions
- Everyday vocabulary

## 🎨 Customization

### Adding New Words
Edit `data/french_words.csv` with new vocabulary:
```csv
French,English
nouveau_mot,new_word
autre_mot,another_word
```

### Changing Appearance
- **Background Color**: Modify `BACKGROUND_COLOR` variable
- **Card Images**: Replace images in the `images/` folder
- **Fonts**: Edit font specifications in the canvas text configurations
- **Timing**: Adjust the auto-flip timer (currently 3000ms)

### UI Modifications
```python
# Change card flip timing (in milliseconds)
flip_time = screen.after(5000, flip_card)  # 5 seconds instead of 3

# Modify colors
BACKGROUND_COLOR = "#your_color_here"

# Change fonts
font=("Arial", 50, "bold")  # Larger, bold text
```

## 🐛 Troubleshooting

### Common Issues

**FileNotFoundError for images**:
- Ensure all image files are in the `images/` folder
- Check that image paths use correct slashes for your OS

**CSV File Errors**:
- Verify `data/french_words.csv` exists and has proper formatting
- The app will create `to_learn.csv` automatically on first run

**Module Import Errors**:
```bash
pip install pandas
# For older Python versions, tkinter might be named differently:
pip install tk
```

## 🚧 Future Enhancements

- [ ] **Audio Pronunciation**: Add text-to-speech for French words
- [ ] **Statistics Dashboard**: Track learning progress and statistics
- [ ] **Multiple Languages**: Support for other language pairs
- [ ] **Difficulty Levels**: Categorize words by difficulty
- [ ] **Spaced Repetition**: Implement advanced spaced repetition algorithm
- [ ] **Dark Mode**: Add theme switching capability
- [ ] **Mobile Version**: Create a mobile-friendly version
- [ ] **Import/Export**: Allow custom vocabulary imports

## 🤝 Contributing

Contributions are welcome! Here are ways you can help:

1. **Add Vocabulary**: Contribute new French-English word pairs
2. **UI Improvements**: Enhance the visual design
3. **Features**: Implement new learning features
4. **Bug Fixes**: Report and fix issues
5. **Documentation**: Improve instructions and documentation

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

## 📚 Learning Tips

- **Consistency**: Study for 10-15 minutes daily rather than long sessions
- **Active Recall**: Try to recall the English meaning before the card flips
- **Review**: Periodically restart with the full word set to reinforce learning
- **Context**: Look up example sentences for words you find difficult


## 🙏 Acknowledgments

- French vocabulary sourced from common word frequency lists
- Built with Python's Tkinter for cross-platform compatibility
- Inspired by the Leitner system of spaced repetition learning

---

**Bonne chance avec votre apprentissage du français! (Good luck with your French learning!)** 🇫🇷✨
