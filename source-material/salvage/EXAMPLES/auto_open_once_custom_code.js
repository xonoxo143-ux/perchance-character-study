// One-time auto-start harness
// Good for runtime automation on imported threads.
// Not clean enough for startup proofs.

if (!oc.thread.customData.autoStarted && oc.thread.messages.length === 0) {
  oc.thread.customData.autoStarted = true;
  setTimeout(() => {
    if (oc.thread.messages.length === 0) {
      oc.thread.messages.push({
        author: 'user',
        content: 'hello',
        expectsReply: true
      });
    }
  }, 0);
}
