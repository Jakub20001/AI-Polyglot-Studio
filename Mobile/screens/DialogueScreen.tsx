import React from 'react';
import { ScrollView, StyleSheet, Text } from 'react-native';
import DialogueCard from '../components/DialogueCard';

const DialogueScreen: React.FC = () => {
    const sampleDialogue = [
        { speaker: 'AI', text: 'Hello! How can I help you today?' },
        { speaker: 'You', text: 'I want to practice ordering food.'},
        { speaker: 'AI', text: "Great! Let's start."},     
    ];

    return (
        <ScrollView contentContainerStyle={styles.container}>
            <Text style={styles.title}>AI Dialogue</Text>
            <DialogueCard dialogue={sampleDialogue}/>
        </ScrollView>
    );
};

export default DialogueScreen;

const styles = StyleSheet.create({
    container: {
        padding: 20,
        flexGrow: 1,
        backgroundColor: '#f9fafb',
      },
      title: {
        fontSize: 24,
        fontWeight: '700',
        color: '#9333ea',
        marginBottom: 16,
      },
});

