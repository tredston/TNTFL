import * as React from 'react';
import { CSSProperties } from 'react';
import { Panel } from 'react-bootstrap';
import { Achievement } from 'tntfl-api';

interface PlayerAchievementProps {
  achievement: Achievement;
  base: string;
}
function PlayerAchievement(props: PlayerAchievementProps): JSX.Element {
  const { achievement, base } = props;
  const icon = 'achievement-' + achievement.name.replace(/ /g, '');
  const opacity = achievement.time ? 1 : 0.3;
  const iconStyle: CSSProperties = {width: 100, textAlign: 'center', opacity};
  return (
    <Panel title={`${achievement.name} - ${achievement.description}`}>
      {achievement.time
        ? <a href={`${base}game/${achievement.time}/`}>
            <div className={icon} style={iconStyle}/>
          </a>
        : <div className={icon} style={iconStyle}/>
      }
    </Panel>
  );
}

interface PlayerAchievementsProps {
  achievements: Achievement[];
  base: string;
}
export default function PlayerAchievements(props: PlayerAchievementsProps): JSX.Element {
  const { achievements, base } = props;
  return (
    <div style={{display: 'flex', flexWrap: 'wrap', justifyContent: 'space-around'}}>
      {achievements.map((a, i) => <PlayerAchievement achievement={a} base={base} key={`${i}`}/>)}
    </div>
  );
}
