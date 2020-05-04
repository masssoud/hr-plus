import moment from 'moment-jalaali'

class JalaliDateHelper {
    static gregorianToJalali = (gregorian, jalaliFormat) => {
        const date = moment(gregorian);
        return date.format(jalaliFormat);
    };

    static humanReadable = (gregorian) => {
        const start = moment(new Date());
        const date = moment(gregorian);
        return date.from(start);
    };
}

export default JalaliDateHelper;
