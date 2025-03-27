import { useState, useEffect, useRef } from "react";
import { Button } from "/components/ui/button";
import { Input } from "/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "/components/ui/card";
import { motion } from "framer-motion";
import { MessageCircle, Send } from "lucide-react";

export default function NegotiationChatbot() {
  const [messages, setMessages] = useState<{ text: string; isUser: boolean }[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [lastOffer, setLastOffer] = useState<number>(50);
  const [isTyping, setIsTyping] = useState(false);
  const minPrice = 45;
  const maxPrice = 60;
  const baseDiscount = 10;
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const handleSendMessage = () => {
    if (inputValue.trim()) {
      setMessages((prev) => [...prev, { text: inputValue, isUser: true }]);
      setInputValue("");
      setIsTyping(true);

      setTimeout(() => {
        const botResponse = generateBotResponse(inputValue);
        setMessages((prev) => [...prev, { text: botResponse, isUser: false }]);
        setIsTyping(false);
      }, 1000);
    }
  };

  const generateBotResponse = (userMessage: string): string => {
    const lowerCaseMessage = userMessage.toLowerCase();

    if (lowerCaseMessage.includes("hello") || lowerCaseMessage.includes("hey")) {
      return "Hello! How can I assist you today?";
    } else if (lowerCaseMessage.includes("i want this shirt")) {
      return `This is a premium shirt! I can only do $${lastOffer}, and only if you decide fast.`;
    } else if (lowerCaseMessage.includes("price")) {
      return `How about $${lastOffer} for this item?`;
    } else if (lowerCaseMessage.includes("yes")) {
      return "Great! You can proceed with the purchase.";
    } else if (lowerCaseMessage.includes("no")) {
      return "Okay, let me know if you change your mind.";
    } else if (lowerCaseMessage.includes("higher")) {
      const newOffer = Math.min(lastOffer + 5, maxPrice);
      setLastOffer(newOffer);
      return `I can go up to $${newOffer}, but that’s my final offer.`;
    } else if (lowerCaseMessage.includes("lower")) {
      const newOffer = Math.max(lastOffer - 5, minPrice);
      setLastOffer(newOffer);
      return `I can go down to $${newOffer}, but that’s my lowest price.`;
    } else if (lowerCaseMessage.includes("warranty")) {
      return "This item comes with a 6-month warranty covering any manufacturing defects.";
    } else if (lowerCaseMessage.includes("discount")) {
      return `I can offer a ${baseDiscount}% discount if you bundle two items or more. If you're a returning customer, I might be able to do a little better!`;
    } else if (lowerCaseMessage.includes("return")) {
      return "We offer a 7-day return policy if the item is unused and in original packaging.";
    } else if (lowerCaseMessage.includes("shipping")) {
      return "Standard shipping takes 3-5 business days. Express shipping is available for an extra fee.";
    } else if (lowerCaseMessage.includes("bulk")) {
      return "For bulk orders, we can provide a special discount. How many units are you interested in?";
    } else {
      return "I'm not sure what you mean. Can you please clarify?";
    }
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <Card className="w-full max-w-2xl mx-auto mt-8 p-6 bg-white shadow-lg rounded-lg">
      <CardHeader>
        <CardTitle className="text-2xl font-bold flex items-center">
          <MessageCircle className="mr-2 h-6 w-6" />
          Negotiation Chatbot
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2 max-h-80 overflow-y-auto bg-gray-50 p-4 rounded-lg">
          {messages.map((message, index) => (
            <motion.div
              key={index}
              className={`flex ${message.isUser ? "justify-end" : "justify-start"}`}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3, delay: index * 0.1 }}
            >
              <div
                className={`p-3 rounded-lg ${
                  message.isUser ? "bg-blue-100 text-blue-800" : "bg-gray-200 text-gray-800"
                } max-w-md`}
              >
                {message.text}
              </div>
            </motion.div>
          ))}
          {isTyping && (
            <motion.div
              className="flex justify-start"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3 }}
            >
              <div className="p-3 rounded-lg bg-gray-200 text-gray-800 italic max-w-md">
                Bot is typing...
              </div>
            </motion.div>
          )}
          <div ref={messagesEndRef} />
        </div>
        <div className="flex space-x-2">
          <Input
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Type a message..."
            className="flex-1"
            onKeyPress={(e) => {
              if (e.key === 'Enter') {
                handleSendMessage();
              }
            }}
          />
          <Button onClick={handleSendMessage} className="bg-blue-500 hover:bg-blue-600">
            <Send className="h-4 w-4" />
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
