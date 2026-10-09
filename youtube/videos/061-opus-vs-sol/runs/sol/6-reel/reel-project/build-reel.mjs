import fs from 'node:fs';

// The supplied SRT repeats one sentence in this window. These corrected
// cues were re-timed from the source audio and checked against the clean
// transcript_057-hermes-agent.txt alongside the original SRT.
const fixes = new Map([
  [3, "done, @coder will open a PR on my"],
  [4, "content repo, save the PR with"],
  [5, "all of the files it's created,"],
  [6, "and then post the link to Slack."],
  [7, "So when I press enter... The report that was"],
  [11, "refresh the Hooks research from the"],
  [13, "reference transcript with a breakdown and"],
  [16, "that to @packager and then @coder."],
  [17, ""],
  [19, "go to another agent first as well. I only"],
  [20, "gave it two agents, but it decided that we"],
  [24, ""],
]);
const escape = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const seconds = t => { const [h,m,rest] = t.split(':'); return Number(h)*3600+Number(m)*60+Number(rest.replace(',','.')); };
const blocks = fs.readFileSync('captions.srt','utf8').trim().split(/\r?\n\s*\r?\n/);
const captions = blocks.map(block => {
  const [num, times, ...lines] = block.split(/\r?\n/);
  const [a,b] = times.split(' --> ');
  return {n:Number(num), start:seconds(a), end:seconds(b), text:fixes.has(Number(num)) ? fixes.get(Number(num)) : lines.join(' ')};
}).filter(c => c.text);
const captionHtml = captions.map(c => `<div class="clip caption" id="caption-${c.n}" data-start="${c.start}" data-duration="${(c.end-c.start).toFixed(3)}" data-track-index="6"><span>${escape(c.text)}</span></div>`).join('\n');
const html = `<!doctype html>
<html lang="en" data-resolution="portrait"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080,height=1920"><title>Bot handoff reel</title><script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#101514;color:#f4f3e9;font-family:Montserrat,sans-serif}
#root{position:relative;width:1080px;height:1920px;overflow:hidden}
#canvas{position:absolute;inset:0;background:#101514}
#top{position:absolute;top:85px;left:72px;right:72px;height:255px;display:flex;flex-direction:column;justify-content:center;border-top:3px solid #a5dc76}
#eyebrow{font:700 27px 'IBM Plex Mono',monospace;letter-spacing:.12em;color:#b8e78e}
#headline{font:400 100px/1 'League Gothic',sans-serif;letter-spacing:.02em;margin:22px 0 0;text-transform:uppercase}
#rule{position:absolute;left:72px;right:72px;top:350px;border-top:2px solid #526257}
#screen-frame{position:absolute;left:45px;top:445px;width:990px;height:825px;border:3px solid #7a9476;border-radius:18px;pointer-events:none;box-shadow:0 35px 90px #050908}
#source-video{position:absolute;left:45px;top:445px;width:1467px;height:825px;object-fit:fill;max-width:none;clip-path:inset(0 477px 0 0 round 16px)}
#screen-label{position:absolute;left:72px;top:405px;font:700 26px 'IBM Plex Mono',monospace;letter-spacing:.08em;color:#d6e0d2}
#chain{position:absolute;left:72px;right:72px;top:1310px;font:700 29px 'IBM Plex Mono',monospace;color:#b8e78e;letter-spacing:.02em}
.caption{position:absolute;left:72px;right:72px;top:1402px;height:250px;display:flex;align-items:flex-start;justify-content:center;text-align:center}
.caption span{display:block;width:100%;font:700 56px/1.22 Montserrat,sans-serif;color:#f9f8ee;text-shadow:0 3px 12px #000,0 5px 28px #000;overflow-wrap:break-word}
#footer{position:absolute;left:72px;right:72px;bottom:130px;border-top:2px solid #526257;padding-top:27px;font:700 23px 'IBM Plex Mono',monospace;letter-spacing:.08em;color:#b9cbbb}
#title-card{position:absolute;left:0;top:0;width:1080px;height:400px;background:#101514;display:flex;flex-direction:column;justify-content:center;padding:46px 72px;z-index:20}
#title-kicker{font:700 26px 'IBM Plex Mono',monospace;color:#b8e78e;letter-spacing:.13em}
#title-main{font:400 102px/.92 'League Gothic',sans-serif;text-transform:uppercase;letter-spacing:.015em;margin:18px 0 16px}
#title-sub{font:700 28px/1.2 Montserrat,sans-serif;color:#c5d3c1;border-top:3px solid #a5dc76;padding-top:14px}
#lower-third{position:absolute;left:72px;top:1120px;width:790px;height:140px;padding:25px 32px;background:#e9f2df;color:#14241a;border-radius:9px;z-index:10}
#lower-third strong{display:block;font:700 32px 'IBM Plex Mono',monospace}
#lower-third small{display:block;margin-top:10px;font:700 26px Montserrat,sans-serif}
</style></head><body><div id="root" data-composition-id="main" data-start="0" data-width="1080" data-height="1920" data-duration="45">
<div id="canvas" data-layout-ignore></div>
<video id="source-video" class="clip" src="source.mp4" data-start="0" data-duration="45" data-track-index="1" muted playsinline></video>
<audio id="source-audio" class="clip" src="source.mp4" data-start="0" data-duration="45" data-track-index="2" data-volume="1"></audio>
<div id="screen-frame" data-layout-ignore></div>
<div id="top" class="clip" data-start="2.6" data-duration="42.4" data-track-index="4"><div id="eyebrow">HERMES AGENT / WORKFLOW</div><h1 id="headline">BOTS HAND OFF THE WORK</h1></div><div id="rule" data-layout-ignore></div>
<div id="screen-label" class="clip" data-start="2.6" data-duration="42.4" data-track-index="5">LIVE DEMO • 057</div><div id="chain">RESEARCHER → PACKAGER → CODER</div>
${captionHtml}
<div id="footer">ONE REQUEST / THREE SPECIALISTS</div>
<div id="title-card" class="clip" data-start="0" data-duration="2.6" data-track-index="10"><div id="title-kicker">HERMES AGENT / 057</div><div id="title-main">ONE REQUEST.<br>THREE BOTS.</div><div id="title-sub">Research → package → pull request</div></div>
<div id="lower-third" class="clip" data-start="17" data-duration="5" data-track-index="9"><strong>THE HANDOFF</strong><small>Researcher → Packager → Coder</small></div>
</div><script>
window.__timelines=window.__timelines||{};
const tl=gsap.timeline({paused:true});
tl.fromTo('#title-main',{y:70,opacity:0},{y:0,opacity:1,duration:.65,ease:'power3.out'},0.1);
tl.fromTo('#title-sub',{y:30,opacity:0},{y:0,opacity:1,duration:.45,ease:'power2.out'},0.6);
tl.fromTo('#lower-third',{x:-80,opacity:0},{x:0,opacity:1,duration:.45,ease:'power3.out'},17.1);
tl.fromTo('#chain',{opacity:.65},{opacity:1,duration:1.2,repeat:20,yoyo:true,ease:'sine.inOut'},2.7);
window.__timelines.main=tl;
</script></body></html>`;
fs.writeFileSync('index.html',html);
console.log(`Built ${captions.length} caption clips from repaired SRT`);
