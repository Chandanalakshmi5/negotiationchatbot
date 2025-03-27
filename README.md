# negotiationchatbot

Overview


The Negotiation Chatbot is an interactive AI-powered chatbot designed to simulate a price negotiation experience for customers. Users can engage in price discussions, inquire about discounts, warranties, returns, and more. The chatbot dynamically adjusts offers and provides responses based on user input.


Features


Real-time Chat Experience: Users can interact with the bot just like a real salesperson.

Price Negotiation: Adjusts pricing based on user responses (higher/lower requests).

Predefined Responses: Handles queries about discounts, warranties, return policies, shipping, and bulk orders.

Typing Indicator: Shows when the bot is "thinking."

Animated Message Display: Uses framer-motion for smooth message transitions.



Technologies Used



React (Frontend framework)

Framer Motion (Animations)

ShadCN UI Components (Button, Input, Card)

TypeScript (For better type safety)



Usage



Type messages into the input box and click Send.

The chatbot will respond based on predefined conditions.

Try negotiating a lower/higher price and see the chatbot adjust accordingly.



Example Interactions:


User: "Hello!"Bot: "Hello! How can I assist you today?"

User: "I want this shirt."Bot: "This is a premium shirt! I can only do $50, and only if you decide fast."

User: "Can you go lower?"Bot: "I can go down to $45, but that’s my lowest price."



Customization


Modify price logic in the generateBotResponse function inside NegotiationChatbot.tsx.

Customize UI styles in Card, Button, and Input components.

Add more responses to cover additional customer interactions.



Future Enhancements


Integration with Payment API for seamless transactions.

Machine Learning-based Dynamic Pricing for smarter negotiations.

Multi-language Support for a global audience.

Chatbot Memory to track past interactions and offer better deals.



Contributing

Fork the repository.

Create a new branch (feature-branch-name).

Commit your changes (git commit -m "Add new feature").

Push to your branch (git push origin feature-branch-name).

Open a Pull Request.

