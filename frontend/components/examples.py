import streamlit as st


def show_examples():

    with st.expander("💡 Example Questions"):

        st.markdown("""
### General Electronics
- What is LM358?
- Explain the working of NE555 Timer.
- What is an Op-Amp?

### Troubleshooting
- My LED is not glowing.
- Why is my transistor heating?
- My 7805 regulator is not giving 5V.

### Circuit Analysis
- Explain this circuit.
- What is the purpose of this circuit?
- Find possible faults in this circuit.

### PDF Chat
- Summarize this datasheet.
- Explain the pin configuration.
- What are the electrical characteristics?

### Code Review
- Review this Arduino code.
- Explain this Verilog module.
- Debug this ESP32 program.
- Optimize this VHDL code.
        """)