import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

interface DialogueLine {
    speaker: string;
    text: string;
}

interface DialogueCardProps {
    dialogue: DialogueLine[];
}

const DialogueCard: React.FC<DialogueCardProps> = ({ dialogue }) => {
    return (
        <View style={styles.card}>
            <Text style={styles.title}>Dialogue</Text>
            {dialogue.map((line, index) => (
                <View key={index} style={styles.lineContainer}>
                    <Text style={styles.speaker}>{line.speaker}:</Text>
                    <Text style={styles.text}>{line.text}</Text>
                </View>
            ))}
        </View>
    );     
};

export default DialogueCard;

const styles = StyleSheet.create({
    card: {
        backgroundColor: '#ffffff',
        padding: 16,
        marginVertical: 12,
        marginHorizontal: 20,
        borderRadius: 12,
        borderWidth: 1,
        borderColor: '#e5e7eb',
        shadowColor: '#000',
        shadowOpacity: 0.05,
        shadowRadius: 4,
        shadowOffset: { width: 0, height: 2}
    },
    title: {
        fontSize: 20,
        fontWeight: '700',
        color: '#2563eb',
        marginBottom: 12,
        textAlign: 'center',
    },
    lineContainer: {
        flexDirection: 'row',
        marginBottom: 8,
        flexWrap: 'wrap',
    },
    speaker: {
        fontWeight: '600',
        color: '#374151',
        marginRight: 6,
    },
    text: {
        color: '#4b5563',
        flexShrink: 1,
    }
});