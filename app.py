import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model('handwritten_math_symbol_recognition_model.h5')  # Replace with your model path

# Create a dictionary to map indices to labels
classes = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: '\\rightarrow', 27: '0', 28: '1', 29: '2', 30: '3', 31: '4', 32: '5', 33: '6', 34: '7', 35: '8', 36: '9', 37: '\\pi', 38: '\\alpha', 39: '\\beta', 40: '\\sum', 41: '\\sigma', 42: 'a', 43: 'b', 44: 'c', 45: 'd', 46: 'e', 47: 'f', 48: 'g', 49: 'h', 50: 'i', 51: 'j', 52: 'k', 53: 'l', 54: 'm', 55: 'n', 56: 'o', 57: 'p', 58: 'q', 59: 'r', 60: 's', 61: 'u', 62: 'v', 63: 'w', 64: 'x', 65: 'y', 66: 'z', 67: '\\Sigma', 68: '\\gamma', 69: '\\Gamma', 70: '\\delta', 71: '\\Delta', 72: '\\zeta', 73: '\\eta', 74: '\\theta', 75: '\\Theta', 76: '\\epsilon', 77: '\\varepsilon', 78: '\\iota', 79: '\\kappa', 80: '\\varkappa', 81: '\\lambda', 82: '\\Lambda', 83: '\\mu', 84: '\\nu', 85: '\\xi', 86: '\\Xi', 87: '\\Pi', 88: '\\rho', 89: '\\varrho', 90: '\\tau', 91: '\\phi', 92: '\\Phi', 93: '\\varphi', 94: '\\chi', 95: '\\psi', 96: '\\Psi', 97: '\\omega', 98: '\\Omega', 99: '\\partial', 100: '\\int', 101: '\\cdot', 102: '\\leq', 103: '\\geq', 104: '<', 105: '>', 106: '\\subset', 107: '\\supset', 108: '\\subseteq', 109: '\\supseteq', 110: '\\cong', 111: '\\propto', 112: '-', 113: '+', 114: '\\mathbb{R}', 115: '\\$', 116: '\\{', 117: '\\copyright', 118: '\\dots', 119: '\\}', 120: '\\S', 121: '\\dag', 122: '\\pounds', 123: '\\&', 124: '\\#', 125: '\\%', 126: '\\checkmark', 127: '\\circledR', 128: '\\mathsection', 129: '\\amalg', 130: '\\cup', 131: '\\oplus', 132: '\\times', 133: '\\ast', 134: '\\triangleleft', 135: '\\otimes', 136: '\\triangleright', 137: '\\diamond', 138: '\\pm', 139: '\\div', 140: '\\bullet', 141: '\\setminus', 142: '\\uplus', 143: '\\cap', 144: '\\mp', 145: '\\sqcap', 146: '\\vee', 147: '\\odot', 148: '\\sqcup', 149: '\\wedge', 150: '\\circ', 151: '\\ominus', 152: '\\star', 153: '\\wr', 154: '\\barwedge', 155: '\\circledcirc', 156: '\\boxdot', 157: '\\ltimes', 158: '\\boxplus', 159: '\\boxtimes', 160: '\\rtimes', 161: '\\circledast', 162: '\\lhd', 163: '\\prod', 164: '\\coprod', 165: '\\oint', 166: '\\parr', 167: '\\with', 168: '\\fint', 169: '\\varoiint', 170: '\\oiint', 171: '\\approx', 172: '\\equiv', 173: '\\not\\equiv', 174: '\\perp', 175: '\\asymp', 176: '\\frown', 177: '\\prec', 178: '\\succ', 179: '\\bowtie', 180: '\\preceq', 181: '\\succeq', 182: '\\mid', 183: '\\vdash', 184: '\\dashv', 185: '\\models', 186: '\\sim', 187: '\\doteq', 188: '\\parallel', 189: '\\simeq', 190: '\\backsim', 191: '\\multimap', 192: '\\pitchfork', 193: '\\therefore', 194: '\\because', 195: '\\between', 196: '\\preccurlyeq', 197: '\\varpropto', 198: '\\Vdash', 199: '\\vDash', 200: '\\nmid', 201: '\\nvDash', 202: '\\sqsubseteq', 203: '\\nsubseteq', 204: '\\subsetneq', 205: '\\varsubsetneq', 206: '\\neq', 207: '\\geqslant', 208: '\\gtrless', 209: '\\lesssim', 210: '\\gtrsim', 211: '\\leqslant', 212: '\\trianglelefteq', 213: '\\blacktriangleright', 214: '\\triangleq', 215: '\\Downarrow', 216: '\\downarrow', 217: '\\Rightarrow', 218: '\\hookrightarrow', 219: '\\Longleftrightarrow', 220: '\\searrow', 221: '\\longmapsto', 222: '\\leftarrow', 223: '\\Longrightarrow', 224: '\\uparrow', 225: '\\Leftarrow', 226: '\\longrightarrow', 227: '\\Leftrightarrow', 228: '\\mapsto', 229: '\\leftrightarrow', 230: '\\nearrow', 231: '\\rightleftharpoons', 232: '\\rightharpoonup', 233: '\\leadsto', 234: '\\circlearrowleft', 235: '\\rightleftarrows', 236: '\\circlearrowright', 237: '\\rightrightarrows', 238: '\\rightsquigarrow', 239: '\\curvearrowright', 240: '\\twoheadrightarrow', 241: '\\nRightarrow', 242: '\\nrightarrow', 243: '\\upharpoonright', 244: '\\mapsfrom', 245: '\\shortrightarrow', 246: '\\lightning', 247: '\\vartheta', 248: '\\varpi', 249: '\\bot', 250: '\\forall', 251: '\\ni', 252: '\\top', 253: '\\ell', 254: '\\hbar', 255: '\\in', 256: '\\notin', 257: '\\wp', 258: '\\exists', 259: '\\Im', 260: '\\Re', 261: '\\nexists', 262: '\\langle', 263: '\\rangle', 264: '\\lceil', 265: '\\rceil', 266: '\\lfloor', 267: '\\rfloor', 268: '[', 269: ']', 270: '|', 271: '\\|', 272: '/', 273: '\\llbracket', 274: '\\rrbracket', 275: '\\vdots', 276: '\\ddots', 277: '\\dotsc', 278: '\\aleph', 279: '\\infty', 280: '\\prime', 281: '\\angle', 282: '\\diamondsuit', 283: '\\sharp', 284: '\\backslash', 285: '\\emptyset', 286: '\\nabla', 287: '\\flat', 288: '\\clubsuit', 289: '\\heartsuit', 290: '\\neg', 291: '\\triangle', 292: '\\sqrt{}', 293: '\\sphericalangle', 294: '\\square', 295: '\\triangledown', 296: '\\blacksquare', 297: '\\lozenge', 298: '\\varnothing', 299: '\\vartriangle', 300: '\\iddots', 301: '\\mathcal{A}', 302: '\\mathcal{B}', 303: '\\mathcal{C}', 304: '\\mathcal{D}', 305: '\\mathcal{E}', 306: '\\mathcal{F}', 307: '\\mathcal{G}', 308: '\\mathcal{H}', 309: '\\mathcal{L}', 310: '\\mathcal{M}', 311: '\\mathcal{N}', 312: '\\mathcal{O}', 313: '\\mathcal{P}', 314: '\\mathcal{R}', 315: '\\mathcal{S}', 316: '\\mathcal{T}', 317: '\\mathcal{U}', 318: '\\mathcal{X}', 319: '\\mathcal{Z}', 320: '\\mathfrak{A}', 321: '\\mathfrak{M}', 322: '\\mathfrak{S}', 323: '\\mathfrak{X}', 324: '\\mathbb{1}', 325: '\\mathds{1}', 326: '\\mathds{C}', 327: '\\mathds{E}', 328: '\\mathds{N}', 329: '\\mathds{P}', 330: '\\mathds{Q}', 331: '\\mathds{R}', 332: '\\mathds{Z}', 333: '\\mathscr{A}', 334: '\\mathscr{C}', 335: '\\mathscr{D}', 336: '\\mathscr{E}', 337: '\\mathscr{F}', 338: '\\mathscr{H}', 339: '\\mathscr{L}', 340: '\\mathscr{P}', 341: '\\mathscr{S}', 342: '\\celsius', 343: '\\degree', 344: '\\ohm', 345: '\\venus', 346: '\\mars', 347: '\\astrosun', 348: '\\fullmoon', 349: '\\leftmoon', 350: '\\female', 351: '\\male', 352: '\\checked', 353: '\\diameter', 354: '\\sun', 355: '\\Bowtie', 356: '\\mathbb{Q}', 357: '\\mathbb{N}', 358: '\\mathbb{Z}', 359: '\\mathbb{H}', 360: '\\ss', 361: '\\aa', 362: '\\L', 363: '\\AA', 364: '\\O', 365: '\\o', 366: '\\ae', 367: '\\AE', 368: '\\guillemotleft'}

def preprocess_image(image):
    img = image.convert('L')  # Convert image to grayscale
    img = img.resize((32, 32))  # Resize to match model input
    img_array = np.asarray(img)
    img_array = img_array.astype('float32') / 255.0  # Normalize
    img_array = img_array.reshape((1, 32, 32, 1))  # Add batch and channel dimensions
    return img_array

def predict_image(image):
    img_array = preprocess_image(image)
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])  # Get index of highest probability
    return classes.get(predicted_index, "Unknown")

# Streamlit UI
st.title('LaTeX Symbol Classifier')
st.write("Upload an image of a LaTeX symbol to get a prediction.")

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    prediction = predict_image(image)
    st.write(f"Predicted Label: {prediction}")
