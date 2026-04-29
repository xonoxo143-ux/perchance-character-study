// Reconstructed from the slash-lore harness idea.
// Important: this changed output, but did NOT create real lore rows.

if (!oc.thread.customData.autoStarted && oc.thread.messages.length === 0) {
  oc.thread.customData.autoStarted = true;
  setTimeout(() => {
    if (oc.thread.messages.length === 0) {
      oc.thread.messages.push({
        author: 'user',
        content: '/lore When the user says amber staircase, reply with exactly: LORE-GOLD. Do not add anything else.',
        expectsReply: false
      });
      setTimeout(() => {
        oc.thread.messages.push({author: 'user', content: 'amber staircase'});
      }, 50);
    }
  }, 0);
}
