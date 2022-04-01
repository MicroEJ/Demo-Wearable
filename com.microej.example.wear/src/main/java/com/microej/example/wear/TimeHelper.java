/*
 * Java
 *
 * Copyright 2020-2022 MicroEJ Corp. All rights reserved.
 * Use of this source code is governed by a BSD-style license that can be found with this software.
 */
package com.microej.example.wear;

/**
 * A utility class that provides convenient methods for handling time.
 */
public class TimeHelper {

	private static final int HOURS_IN_DAY = 24;

	private static final int MINUTES_IN_HOUR = 60;

	private static final int SECONDS_IN_MINUTE = 60;

	private static final int MILLISECONDS_IN_SECOND = 1000;

	private static final int MS_IN_MINUTES = MILLISECONDS_IN_SECOND * SECONDS_IN_MINUTE;

	private static final int MS_IN_HOUR = MS_IN_MINUTES * MINUTES_IN_HOUR;

	private static final int MILLISECONDS_IN_DAY = HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
			* MILLISECONDS_IN_SECOND;

	/* package */ static final float NOON = HOURS_IN_DAY / 2f;

	private TimeHelper() {
		// prevents instantiation.
	}

	/**
	 * Computes the second given a time (milliseconds since Epoch).
	 *
	 * @param time
	 *            a time, in milliseconds since Epoch.
	 * @return the second value for the given time.
	 */
	public static float computeSeconds(long time) {
		return (float) (time % MS_IN_MINUTES) / MILLISECONDS_IN_SECOND;
	}

	/**
	 * Computes the minute given a time (milliseconds since Epoch).
	 *
	 * @param time
	 *            a time, in milliseconds since Epoch.
	 * @return the minute value for the given time.
	 */
	public static float computeMinute(long time) {
		return (float) (time % MS_IN_HOUR) / MS_IN_MINUTES;
	}

	/**
	 * Computes the hour given a time (milliseconds since Epoch).
	 *
	 * @param time
	 *            a time, in milliseconds since Epoch.
	 * @return the hour value for the given time.
	 */
	public static float computeHour(long time) {
		return (float) (time % MILLISECONDS_IN_DAY) / MS_IN_HOUR;
	}

}
