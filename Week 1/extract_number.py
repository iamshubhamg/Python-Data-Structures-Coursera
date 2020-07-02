text = "X-DSPAM-Confidence:    0.8475";text = "X-DSPAM-Confidence:    0.8475";
startPos = text.find(':')
piece = text[startPos+1:]
end = float(piece)
print(end)
