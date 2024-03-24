import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)


warnings.warn("No code here", SyntaxWarning)
try:
    warnings.warn("Import warning", ImportWarning)
except ImportWarning:
    print("Except Import warning ")

print("End program")
